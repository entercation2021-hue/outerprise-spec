# Outerprise specification surface

External Evidence Delivery: Separating Content Integrity, Claimed Time, and Institutional Receipt. An Entercation implementation note.

This repository is a draft examination surface for the Outerprise evidence-delivery model. It is intentionally explicit about what is a cryptographic property, what is a participant assertion, what is an institutional receipt, and what is a sponsor/project identity binding.

## Start here

- [Knowledge Library index](https://outerprise-knowledge-library.lovable.app)
- [Trust and non-inheritance statement](./TRUST.md)
- [Canonical Knowledge Library compilation](./canonical/knowledge-library.md)
- [Authoritative 105-page Examination Edition PDF](./book/Surprise_Outerprise_Examination_Edition_105_Pages.pdf)
- [Short draft alignment note](./book/surprise-outerprise-examination-edition.md)
- [Repository file-hash manifest](./digests/canonical-digests.json)
- [Verification scripts](./scripts/)
- [Citation metadata](./CITATION.cff)
- [MIT License](./LICENSE)

## Scope and status

These files are draft specifications, not legal advice, an audit opinion, or a claim that any named system has accepted a record. A hash proves equality with the bytes hashed; it does not prove authorship, truth, time of creation, delivery, receipt, or sponsor/project pairing.

The supplied `book/Surprise_Outerprise_Examination_Edition_105_Pages.pdf` is the authoritative examination-book artifact in this repository. It is preserved byte-for-byte from the supplied file and is not silently converted into the short Markdown note. The Markdown file is a separate, from-scratch alignment companion and must not be cited as the original 105-page book.

OPD names the package-delivery relationship. The authoritative book records **Outer Package Delivery** on the current board and **Outerprise Package Delivery** in earlier vocabulary; this repository uses the latter as its expanded form. Pair Key is the concatenation of a 64-hex sponsor identity hash and a 64-hex project identity hash, producing a 128-hex relationship identifier. It is not a signature, password, or login.

The repository manifest records SHA-256 file hashes for reproducibility. Those hashes are repository integrity checks; they are not Pair Key values, not Dual Attestation recipes, and not institutional receipts. The artifacts are hashed as exact bytes. Run the verifiers from the repository root:

```bash
python3 scripts/verify_digests.py
node scripts/verify_digests.mjs
python3 scripts/verify_test_vectors.py
```
