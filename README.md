# Outerprise specification surface

External Evidence Delivery: Separating Content Integrity, Claimed Time, and Institutional Receipt. An Entercation implementation note.

This repository is a from-scratch draft examination surface for the Outerprise evidence-delivery model. It is intentionally explicit about what is a cryptographic property, what is a participant assertion, and what is an institutional receipt.

## Start here

- [Knowledge Library index](https://outerprise-knowledge-library.lovable.app)
- [Trust and non-inheritance statement](./TRUST.md)
- [Canonical digest manifest](./digests/canonical-digests.json)
- [Verification scripts](./scripts/)

## Scope and status

These files are draft specifications, not legal advice, an audit opinion, or a claim that any named system has accepted a record. A hash proves equality with the bytes hashed; it does not prove authorship, truth, time of creation, delivery, or receipt.

The canonical artifacts are UTF-8 Markdown files with LF line endings. Their SHA-256 values are recorded in `digests/canonical-digests.json`. Run either verifier from the repository root:

```bash
python3 scripts/verify_digests.py
node scripts/verify_digests.mjs
```

The standard SHA-256 test vectors are in [`test-vectors/sha256.json`](./test-vectors/sha256.json) and can be checked with:

```bash
python3 scripts/verify_test_vectors.py
```
