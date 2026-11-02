# Outerprise Knowledge Library — Canonical Compilation

**Canonical artifact:** file-integrity hash input. UTF-8 Markdown, LF line endings, final newline.

This compilation is a draft alignment surface grounded in the supplied examination book. Individual readable exports are linked from [the root index](../index.md). It does not silently replace the source book’s vocabulary or identity rules.

---

## 1. Integration Paradox

The more systems participate in an evidence workflow, the more carefully the workflow must separate content identity, claimed event time, institutional receipt, and sponsor/project identity binding. Let `C` be a byte string and `H(C)` its SHA-256 hash. `same(C, C')`, `hash_equal(C, d)`, `claimed_at(t_c)`, `received(R)`, and `paired(sponsor, project)` are different predicates. In general, none implies any other. A hash proves equality for specified bytes and an algorithm; it does not prove truth, authorship, time, receipt, or sponsor/project pairing.

## 2. Pair Key / Dual Attestation

A Pair Key identifies one sponsor and one project together. It is the concatenation of a 64-character hexadecimal sponsor identity hash and a 64-character hexadecimal project identity hash, producing a 128-character hexadecimal relationship identifier:

```text
pair_key = sponsor_identity_hash || project_identity_hash
```

The join is not a new signature, password, login, or proof that funds were received. A separate Dual Attestation recipe must not be inferred from the Pair Key identity join.

## 3. OPD — Outerprise Package Delivery

OPD names the package-delivery relationship. The authoritative examination book records **Outer Package Delivery** on the current board and **Outerprise Package Delivery** in earlier vocabulary. This repository uses Outerprise Package Delivery as its expanded form and preserves the source distinction. OPD is not “Outerprise Proof Document.” An OPD may carry package references, integrity hashes, Pair Key references, claimed times, delivery attempts, receipt data, provenance, and limitations. These fields make delivery inspectable; they do not manufacture proof or transfer authority.

## 4. Outer-Gration

Outer-Gration is the controlled movement of an evidence artifact from an originating operational context to an external receiving context. It is a boundary operation, not a claim that the contexts share authority. “Sent,” “delivered,” “opened,” “accepted,” and “acted upon” are distinct statuses and must not be promoted without evidence for the additional transition.

## 5. Claimed Time vs. Institutional Receipt

A sender may assert `t_c`, while a receiving institution may record `t_r`. The safe representation labels them separately with their asserting or recording party, basis, timezone, precision, and limitations. The ordering `t_c ≤ t_r` is operationally plausible but not a theorem of the data model without a trusted time basis.

## 6. Evidence Delivery Contract

For each delivery, create an integrity hash, identify the representation and sender, record any Pair Key reference separately, create a delivery attempt, and—if available—obtain a receiver receipt bound to the same package hash. Use narrow statuses such as `hash_verified`, `sender_claim_recorded`, `delivery_attempt_recorded`, and `receipt_verified`. Avoid an undifferentiated `verified` label.

## File-hash note

The repository manifest records hashes of committed files for reproducibility. Those file hashes are integrity checks for this repository’s bytes. They are not the Pair Key, not a Dual Attestation recipe, and not an institutional receipt.
