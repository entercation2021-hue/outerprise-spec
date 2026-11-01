# Outerprise Knowledge Library — Canonical Compilation

**Canonical artifact:** D1 input. UTF-8 Markdown, LF line endings, final newline.

This compilation is the canonical from-scratch draft of the Knowledge Library. Individual readable exports are linked from [the root index](../index.md).

---

## 1. Integration Paradox

The more systems participate in an evidence workflow, the more carefully the workflow must separate content identity, claimed event time, and institutional receipt. Let `C` be a byte string, `H(C)` its SHA-256 digest, `t_c` a sender-claimed time, and `R` a receiver receipt record. `same(C, C')`, `digest_equal(C, d)`, `claimed_at(t_c)`, and `received(R)` are different predicates. In general, none implies any other. A digest proves equality for specified bytes and an algorithm; it does not prove truth, authorship, time, or receipt.

## 2. Pair Key / Dual Attestation

A pair key is a conceptual protocol object containing two independently attributable attestations: a content attestation by the sender or producer and a receipt attestation by the receiving institution or service. Both attestations should bind to the same content digest. Forwarding a sender attestation does not make it a receiver attestation, and a receiver attestation that bytes were received does not validate the sender’s claims about those bytes.

## 3. OPD — Outerprise Proof Document

An OPD is a typed evidence envelope. Its conceptual fields include version, payload or reference, content digest, claimant, claimed time, delivery attempt, receipt, provenance, and limitations. An OPD makes boundaries inspectable; it does not manufacture authority. A transformed artifact has a new digest unless the exact bytes remain unchanged.

## 4. Outer-Gration

Outer-Gration is the controlled movement of an evidence artifact from an originating operational context to an external receiving context. It is a boundary operation, not a claim that the contexts share authority. “Sent,” “delivered,” “opened,” “accepted,” and “acted upon” are distinct statuses and must not be promoted without evidence for the additional transition.

## 5. Claimed Time vs. Institutional Receipt

A sender may assert `t_c`, while a receiving institution may record `t_r`. The safe representation labels them separately with their asserting or recording party, basis, timezone, precision, and limitations. The ordering `t_c ≤ t_r` is operationally plausible but not a theorem of the data model without a trusted time basis.

## 6. Evidence Delivery Contract

For each delivery, create a digest, identify the representation and sender, create a delivery attempt, and—if available—obtain a receiver receipt bound to the same digest. Use narrow statuses such as `digest_verified`, `sender_claim_recorded`, `delivery_attempt_recorded`, and `receipt_verified`. Avoid an undifferentiated `verified` label.
