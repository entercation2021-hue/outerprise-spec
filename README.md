# Outerprise specification surface

**External Evidence Delivery: Separating Content Integrity, Claimed Time, and Institutional Receipt. An Entercation implementation note.**

This repository is a from-scratch draft examination surface for the Outerprise evidence-delivery model. It is intentionally explicit about what is a cryptographic property, what is a participant assertion, and what is an institutional receipt.

## Start here

- [Knowledge Library index](index.md)
- [Trust and non-inheritance statement](TRUST.md)
- [Examination Edition](book/surprise-outerprise-examination-edition.md)
- [Canonical digest manifest](digests/canonical-digests.json)
- [Verification scripts](scripts/README.md)

## Scope and status

These files are draft specifications, not legal advice, an audit opinion, or a claim that any named system has accepted a record. The terms “Supabase,” “Lovable,” and “Entercation” are used only to describe the three-layer carve-out in [TRUST.md](TRUST.md). A hash proves equality with the bytes hashed; it does not prove authorship, truth, time of creation, delivery, or receipt.

The canonical artifacts are UTF-8 Markdown files with LF line endings. Their SHA-256 values are recorded in [`digests/canonical-digests.json`](digests/canonical-digests.json). Run either verifier from the repository root:

```bash
python3 scripts/verify_digests.py
node scripts/verify_digests.mjs
```

Both scripts must report success before a digest claim is treated as reproducible.
