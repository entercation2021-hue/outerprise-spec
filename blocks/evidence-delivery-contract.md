# Evidence Delivery Contract

**Status:** Draft Knowledge Library block.

## Minimal protocol

For each delivery, the sender creates a content digest, records the artifact and its representation, identifies the sender, and creates a delivery attempt. The receiver, if willing and able, returns a receipt that binds to the digest and identifies its own receipt time and status.

## Verification checklist

- Are the bytes available or is the reference resolvable?
- Is the digest algorithm stated and recomputable?
- Does the computed digest equal the claimed digest?
- Is the sender identity and attestation mechanism stated?
- Is the claimed time clearly labeled and qualified?
- Is there a separate receiver receipt?
- Does the receipt bind to the same digest?
- Are transformations, retries, and limitations recorded?
- Does the conclusion avoid claiming truth or institutional endorsement beyond the evidence?

## Result vocabulary

Use narrow statuses such as `digest_verified`, `sender_claim_recorded`, `delivery_attempt_recorded`, `receipt_verified`, and `institutional_action_not_established`. Avoid an undifferentiated `verified` label.
