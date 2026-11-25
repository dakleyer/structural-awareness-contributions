# Dual-time, provenance-bound certificate contract — SA-O2/O5 → EA review

**Research integration · 28 October 2026 · v0.1 · Owner: Iván Abril Palma / The Integral Management Society**

## 1. Original problem and corpus lineage

An event $e$ can occur at time $t_1$ and be held in a **pre-admission, unresolved** observation store. A later admissible source rule $q$, issued at $t_2$, can requalify what that already-preserved event means for a named receiving question. A certificate with an end-of-use window at $t_3$ cannot justify **a new decision at $t_{10}$** even though a historical reading of $e$ remains available. These are distinct questions. The old boolean-only online-context exercise checked event time against expiry and thereby allowed a valid-at-event/expired-at-use confusion.

The implementation stays at the place assigned by the corpus:

1. **SA-O2:** retain a material observational difference before its meaning is known, where permitted; loss before capture is irreversible. Retention is not qualification.
2. **SA-O5:** a qualified new interpretive rule can re-read retained evidence for a particular question. Neither a retained fragment nor a new rule confers authority on its own.
3. **SA-O4:** a finite guard shortcut is admissible only within its proven typed domain; certificate validity must never widen proof scope.
4. **00M §4.1 F1 / PR60 §02 D1:** judge whether the *receiving question* and the *eligible operation signature* can be answered through A. A richer A+Q projection is admissible only after evidence Q is source-qualified and allowed for that receiver/use.
5. **00M §6.2:** numeric gain is a **different downstream comparison**. No certificate produces economic gain, a C/D role, an action, consciousness, or an EA/RA/MSCA runtime by itself.

The same receiving-side rule applies to the social old/new joint-capacity case and the agentic AG01/AG02 fixed-transfer case. It is not specific to either numerical example.

## 2. Reusable data model

The module [`qualified_certificates.py`](./qualified_certificates.py) is standard-library Python and does not import ACC, PR57 or any domain application.

| Object | Provenance and scope bound into its signed content |
|---|---|
| `RetainedEvent` | event ID and kind; **claimed** origin (not independently verified external origin); observer/key; SHA-256 of actual payload; scope, context version, time basis; occurred/captured/retention times; signed capture flag; fixed `UNRESOLVED` admission |
| `RuleCertificate` | issuer/key, source owner/roles/method/evidence reference; exact event ID/kind/origin/payload hash, observer/key and **hash of the entire event record**; scope/context; receiver, purpose, question, rule version; separate historical event coverage, issuance and current-use windows |
| `DecisionUse` | the receiving decision ID, scope, context/rule versions, authenticated receiver, purpose, question, **time basis**, declared decision time |
| `RevocationReceipt` | authority/key, subject issuer/key/certificate ID/**certificate-content SHA-256**; CLEAR/FORWARD_REVOKED/RETRO_REVOKED/UNKNOWN; time basis, status-observation time, end of freshness and revocation-effective time |
| `CertificateAssessment` | **separate** `historical_status` and `use_status`; event/certificate/decision IDs; `execution="NEVER"` |

Each signed type has distinct domain-separated canonical JSON bytes. The verification interface accepts a key-management/HSM/public-key backend; `sign_hmac` and `verify_hmac` supply a small, deterministic shared-key **reference and test** backend, with no runtime key embedded in the module.

**Coverage and use are independent half-open intervals:** `[event_from,event_until_exclusive)` and `[use_from,use_until_exclusive)`. Retention and revocation freshness also use exclusive upper bounds. Time inputs are exact nonnegative integers, not floats, booleans, strings, mixed monotonic clocks or accidental timezone conversions. Every record carries an explicit clock domain.

## 3. Decision procedure

The decision function verifies, in sequence:

1. Existence, type and **cryptographic integrity of the event** before trusting its capture claims; trusted clock in the event's named domain; positive local maximum revocation age.
2. Independent capture permission, rights to keep/read the record, retention window, and **availability of the underlying payload**. A digest with missing retained content is no replay source.
3. Signed rule certificate, exact event-record binding, historical coverage, **source-method/role qualification by an independent policy**, and issuance by the current verification time.
4. Independently signed revocation receipt matching the exact certificate **content** as well as issuer/key/ID. Its status cannot predate the certificate, be in a different clock domain, be in the future, be outside its signed freshness window or exceed the receiving system's stricter age cap. An independent latest-state check must rule out **replayed earlier CLEAR receipts**. UNKNOWN, outage, old CLEAR or forged CLEAR never means unrevoked.
5. A retroactive revocation effective now invalidates the historical basis. Forward-only revocation preserves the retrospective record, but stops current use after its effective time.
6. Historical interpretation is reported separately. Current use additionally requires equal trusted and declared decision times, matching clock domain, authenticated receiver, exact receiver/purpose/question/scope, no effective forward revocation, a currently live rule window, matching context/rule versions, and separately granted evidence-use rights.

All policy callbacks require an actual boolean True. False denies; an exception, None, string, integer or unavailable authority gives an explicit unknown/denial status. The event's signed `capture_permitted` flag or rule's signed `source_role` label **cannot grant an independent right**.

A receiving integration configures:
- `verify_attestation(record)`: authenticity of observer/issuer/revocation signatures, including key validity and trust anchors.
- `trusted_clock(time_basis)`: authoritative clock in that domain.
- `capture_right(event)`, `retention_right(event,decision)`, `payload_available(event)`: source preservation and lawful availability.
- `source_qualified(certificate,event)`: qualification of method, owner and role at this receiver, **not** a label self-assertion.
- `revocation_current(receipt,certificate,now)`: latest authoritative state/checkpoint; signed stale-status replay is rejected.
- `request_authenticated(decision)` and `evidence_use_right(certificate,decision)`: receiver identity, allowed purpose and use.
- `max_revocation_age`: locally imposed, positive freshness bound, overriding a longer signed TTL.

### Example: the temporal defect repaired

All numbers below are **fixture ticks**, not wall-clock timestamps.

| Observation / use | Historical result | Current-use result |
|---|---|---|
| (t_1=1): event occurred/captured, unresolved; certificate not issued | `UNRESOLVED` | `CERTIFICATE_NOT_YET_ISSUED` |
| (t_2=2): certificate issued and current revocation evidence verified | `HISTORICALLY_APPLICABLE` | `VALID_FOR_CURRENT_REVIEW` |
| (t_3=3): exact expiry, exclusive endpoint | `HISTORICALLY_APPLICABLE` | `EXPIRED_AT_USE` |
| (t_{10}=10): original event still retained, certificate expired | `HISTORICALLY_APPLICABLE` | `EXPIRED_AT_USE` |
| At $t_{10}$, caller lies and declares decision-time $t_2$ | `HISTORICALLY_APPLICABLE` | `DECISION_TIME_NOT_CURRENT` |
| Source event was discarded before capture, or retained payload lost | `NO_REPLAY_SOURCE` / `RETAINED_PAYLOAD_MISSING` | `NO_LIVE_EVIDENCE` |
| A signed CLEAR receipt is outdated/superseded | `REVOCATION_STALE` / `REVOCATION_SUPERSEDED` | `REVOCATION_STALE` / `REVOCATION_UNKNOWN` |

Historical applicability here means that **this preserved event can be interpreted under this source-qualified rule within this verified audit state**; it does not mean the claim is universally true, that an expired rule is currently usable, or that the receiver may act. A currently withdrawn certificate can be distinguished as forward-withdrawn versus retrospectively invalidated.

## 4. Integration with finite structural adequacy

The receiving adapter first evaluates signed evidence, then decides whether an additional Q **may** be exposed to `structural_adequacy.assess_finite_adequacy` as a qualified part of A+Q. If the rule is expired, Q remains hidden from *current* review; the pre-existing A retains its F1/D1 witness. If the source is unqualified and only part of the evidence is known, the case is **UNKNOWN**, not spuriously deemed adequate because other cases happened to receive extra fields.

The cross-model tests use the actual finite numbers already attached to the research:

- **Social:** same old public capacity 8, joint prospective outcomes 10 vs 8; unqualified old A hides the joint distinction.
- **Agentic:** same public A, PR57 AG01/AG02 fixed-transfer physical outputs 11.5 vs 8.875; current output at A alone was 10 in both.

Both retain their structural problem at $t_{10}$, even if an expired certificate can still describe the old event. Both can be separated with eligible, correctly bound Q at $t_2$. The tests deliberately leave the independently authored model source and numeric referee intact.

## 5. Threat/negative-control matrix

| Attack or defect | Required outcome |
|---|---|
| Change a signed event's origin, observer, capture date, rights, payload hash or scope | Invalid event signature, or **exact event-record binding** failure for a newly signed different event |
| Copy one certificate to another event/payload/observer, purpose or receiver | Event-binding or receiving-contract mismatch |
| Reissue the same certificate ID with altered signed content while reusing old CLEAR | **Certificate fingerprint** mismatch |
| Reuse a signed CLEAR before certificate issuance or after more recent revocation | Reject as pre-issuance or superseded; not a valid unrevoked status |
| Extend an issuer's generous signed status expiry beyond local allowed age | Local freshness failure |
| Move a certificate to an incompatible clock, context or rule version | Clock-domain or decision-frame mismatch |
| Claim a past decision time to reuse expired source at a later real time | Trusted-current-time mismatch |
| Change signer key, use an unknown issuer, tamper with signatures, simulate verifier outage | Fail closed |
| Make an unauthorized trace seem qualified by marking admission TRUE | Type/admission rejection; independent rights/source checks |
| Lose or never store the retained payload | No historical requalification, even with a purported certificate |
| Present one qualified A+Q row but an unqualified second observation | Structural **UNKNOWN**, not a false F1/D1 adequacy proof |
| Attempt action from a valid review certificate | **No action path exists**; `execution` remains `NEVER` |

## 6. Verification and decision boundary

Run in the research-study directory:

```bash
python3 -B -m unittest discover -s . -p 'test_theme18_*.py' -v
```

`test_theme18_certificates.py` checks independent time axes, proof replay, content hashes, source/capture/retention/use rights, current authorization, status freshness, retroactive/forward revocation, tampering, error paths and the same reusable contract **against both social and agentic finite F1/D1 controls**. `test_theme18_online_context.py` no longer implements the old `requalify(retained, certificate)` dictionary+boolean shortcut; it treats raw capture as unresolved and routes attempted requalification to the signed interface. Other F1/D1 and gain tests retain their distinct responsibilities.

**Design boundary:** the result is an *auditable admission-for-review primitive*. It is neither a source authenticator by fiat nor a complete distributed PKI, revocation ledger, RA/EA runtime, physical referee or actuation controller. A real deployment must supply its own actual authenticated authorities, clock, source qualifications, latest revocation view and retained-payload store through the **mandatory named interfaces above**. Those interfaces are the system boundary, not hidden permissive defaults.

Nothing here rewrites 00M/00N or declares that an informational certificate creates a measurable net gain. This v0.1 is an inspectable addition to the independent PR60 research branch pending owner/source audit.
