#!/usr/bin/env python3
"""Check package preservation only; does not execute model/DDS/UC21 experiments."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
data = json.loads((root / "coverage/paragraphs.json").read_text(encoding="utf-8-sig"))
assert len(data["sources"]) == 4
assert len(data["units"]) == 1441
assert len({u["unit_id"] for u in data["units"]}) == 1441
for source in data["sources"]:
    units = [u for u in data["units"] if u["source_id"] == source["source_id"]]
    assert len(units) == source["paragraphs"]
    text = (root / source["source_book"]).read_text(encoding="utf-8-sig")
    chunks = re.split(r"<!-- (S[1-4]-P[0-9]{4}) -->\n\n", text)
    assert len(chunks) == 1 + 2*len(units)
    for i, unit in enumerate(units):
        assert chunks[1+2*i] == unit["unit_id"]
        paragraph = chunks[2+2*i].rstrip("\n")
        paragraph = re.sub(r'^<a id="s[1-4]-p[0-9]{4}"></a>\n\n', "", paragraph, count=1)
        if paragraph != unit["text"]:
            assert re.sub(r"^#{1,4} ", "", paragraph, count=1) == unit["text"]
assert sum(u["private_locator_redacted"] for u in data["units"]) == 20
main = [u for u in data["units"] if u["source_id"] == "S1"]
assert len(main) == 1045
assert len({u["source_block"] for u in main}) == 29
assert {u["prior_action_id"] for u in main if u["prior_action_id"]} == set(range(1,15)) - {11}
assert any("IQ-06" in u["text"] and "Ormuz" in u["text"] for u in main)
plan = (root / "DDS_EVALUATION_PLAN.md").read_text(encoding="utf-8-sig")
assert re.findall(r"\| ACC-ECO-(\d+) \|", plan) == [f"{i:02}" for i in range(1,23)]
print(json.dumps({"source_documents":4, "source_paragraphs":1441, "main_source_paragraphs":1045, "main_blocks":29, "new_action_passages":13, "ormuz_preexisting":True, "private_locator_redacted_paragraphs":20, "proposed_contrasts":22, "model_experiments_executed":False}, ensure_ascii=False))
