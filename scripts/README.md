# Repository file-hash verification scripts

The canonical manifest records SHA-256 hashes of two committed artifacts:

- `knowledge_library` is the hash of `canonical/knowledge-library.md`.
- `examination_book_pdf` is the hash of the exact supplied bytes of `book/Surprise_Outerprise_Examination_Edition_105_Pages.pdf`.

These are repository reproducibility hashes. They are **not** Pair Key values, are **not** Dual Attestation recipes, and do **not** establish institutional receipt. The separate short Markdown examination note is not the authoritative 105-page book and is not the book hash input.

The verifiers read raw bytes; they do not parse Markdown or PDF, trim whitespace, or normalize Unicode. Run from the repository root:

```bash
python3 scripts/verify_digests.py
node scripts/verify_digests.mjs
python3 scripts/verify_test_vectors.py
```

The scripts compare computed values to `digests/canonical-digests.json`, verify that the declared algorithm is `SHA-256`, and exit nonzero on any mismatch or missing file.
