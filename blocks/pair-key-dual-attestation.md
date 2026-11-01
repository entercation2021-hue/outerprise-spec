# Pair Key / Dual Attestation

**Status:** Draft Knowledge Library block.

## Purpose

A pair key is a conceptual protocol object containing two independently attributable attestations: a **content attestation** by the sender or producer, and a **receipt attestation** by the receiving institution or service.

## Minimal shape

```text
PairKey = {
  content_digest: H(C),
  content_attestor: A_s,
  claimed_time: t_c,
  receipt_digest: H(receipt_record),
  receipt_attestor: A_r,
  receipt_time: t_r,
  linkage: identifier binding the receipt to H(C)
}
```

The receipt should bind to the content digest, not merely to a mutable display label. If a receiver cannot authenticate its receipt attestation, the field may be recorded as an unverified claim rather than treated as institutional proof.

## Non-implication

A sender attestation does not become a receiver attestation through forwarding. Likewise, a receiver attestation that it received bytes does not attest that the sender’s claims about those bytes are true.

## Verification rule

A verifier checks the content digest against the received content, authenticates the sender attestation under its stated key or mechanism, authenticates the receipt attestation under the receiver’s stated mechanism, and confirms that both attestations bind to the same digest. Failure of any check must be visible rather than silently collapsed into “verified.”
