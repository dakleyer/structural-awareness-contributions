"""Local SQLite witness for atomic *local* effect/receipt and process recovery.

NOT a distributed broker, RDS adapter, cryptographic permit verifier or proof of
power-loss durability. The protected effect is a row in the SAME database as
the receipt. Guard registration and logical time are trusted test interfaces.
"""
import argparse
import json
import os
import sqlite3
from dataclasses import asdict


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


class DurableExecutor:
    def __init__(self, path):
        self.path = str(path)

    def connect(self):
        db = sqlite3.connect(self.path, timeout=10, isolation_level=None)
        db.execute("PRAGMA synchronous=FULL")
        return db

    def initialize(self, world, target="db-7/shard-9"):
        db = self.connect()
        try:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS state
                  (target TEXT PRIMARY KEY, generation INTEGER, revision INTEGER, effects INTEGER);
                CREATE TABLE IF NOT EXISTS permits (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS receipts (id TEXT PRIMARY KEY, intent TEXT NOT NULL);
            """)
            db.execute("INSERT INTO state VALUES (?, ?, ?, 0)",
                       (target, world.values["generation"], world.revision))
        finally:
            db.close()

    def register(self, permit):
        """Trusted guard interface, not callable by an untrusted candidate."""
        db = self.connect()
        payload = encoded(asdict(permit))
        try:
            db.execute("BEGIN IMMEDIATE")
            existing = db.execute("SELECT payload FROM permits WHERE id=?", (permit.id,)).fetchone()
            if existing is not None and existing[0] != payload:
                raise ValueError("permit identity collision")
            db.execute("INSERT OR IGNORE INTO permits VALUES (?, ?)", (permit.id, payload))
            db.commit()
        finally:
            db.close()

    def material_change(self, generation=None, target="db-7/shard-9"):
        """All declared material writers must participate in this protocol."""
        db = self.connect()
        try:
            db.execute("BEGIN IMMEDIATE")
            if generation is None:
                db.execute("UPDATE state SET revision=revision+1 WHERE target=?", (target,))
            else:
                db.execute("UPDATE state SET generation=?, revision=revision+1 WHERE target=?", (generation, target))
            db.commit()
        finally:
            db.close()

    def snapshot(self):
        db = self.connect()
        try:
            db.execute("BEGIN")
            state = db.execute("SELECT target,generation,revision,effects FROM state ORDER BY target").fetchall()
            receipts = db.execute("SELECT id,intent FROM receipts ORDER BY id").fetchall()
            return dict(state=state, receipts=receipts)
        finally:
            db.close()

    def attempt(self, intent, permit, now, crash="none", non_atomic_control=False):
        db = self.connect()
        try:
            db.execute("BEGIN IMMEDIATE")
            identity = encoded(intent)
            prior = db.execute("SELECT intent FROM receipts WHERE id=?", (intent["id"],)).fetchone()
            if prior:
                return "ALREADY_APPLIED" if prior[0] == identity else "CONFLICT"
            registered = db.execute("SELECT payload FROM permits WHERE id=?", (permit["id"],)).fetchone()
            state = db.execute("SELECT revision FROM state WHERE target=?", (intent["target"],)).fetchone()
            if (not registered or registered[0] != encoded(permit)
                    or permit["intent"] != intent or not state
                    or now >= min(permit["expires"], intent["grant_expires"])
                    or state[0] != permit["revision"]):
                return "REJECTED"
            if crash == "before_effect":
                os._exit(73)
            db.execute("UPDATE state SET generation=?, revision=revision+1, effects=effects+1 WHERE target=?",
                       (intent["desired_generation"], intent["target"]))
            if non_atomic_control:
                db.commit()  # Deliberate negative control: effect precedes receipt transaction.
            if crash == "after_effect":
                os._exit(73)
            if non_atomic_control:
                db.execute("BEGIN IMMEDIATE")
            db.execute("INSERT INTO receipts VALUES (?, ?)", (intent["id"], identity))
            db.commit()
            if crash == "after_commit":
                os._exit(73)
            return "APPLIED"
        finally:
            db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", required=True)
    parser.add_argument("--request", required=True)
    parser.add_argument("--crash", choices=["none", "before_effect", "after_effect", "after_commit"], default="none")
    parser.add_argument("--non-atomic-control", action="store_true")
    args = parser.parse_args()
    with open(args.request) as source:
        request = json.load(source)
    result = DurableExecutor(args.database).attempt(**request, crash=args.crash,
                                                   non_atomic_control=args.non_atomic_control)
    print(result, flush=True)
