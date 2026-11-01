# OPD — Outerprise Proof Document

**Status:** Draft Knowledge Library block.

## Definition

An Outerprise Proof Document (OPD) is a typed evidence envelope. It does not manufacture authority; it makes the boundaries of a claim inspectable.

## Required conceptual fields

```text
opd_version
payload_or_payload_reference
content_digest { algorithm, value, encoding }
claimant { id, role }
claimed_time { value, timezone, precision, basis }
delivery { channel, attempt_id, sent_at }
receipt { status, receiver, received_at, evidence_reference }
provenance { producer, transformations[] }
limitations[]
```

A field may be `unknown`, `not asserted`, or `not available`; omission must not be interpreted as confirmation.

## Digest rule

For a payload `C`, calculate `d = SHA-256(UTF8(C))` only when the encoding and canonical byte representation are specified. If a document is transformed, the transformed artifact has a new digest; it is not the same artifact merely because its rendered text appears equivalent.

## Proof boundary

An OPD can make evidence easier to verify. It cannot turn an unsupported claim into a fact, and it cannot transfer institutional authority from one named layer to another.
