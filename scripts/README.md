# Digest verification scripts

The canonical digest manifest defines two digests:

- **D1** is SHA-256 over the exact UTF-8 bytes of `canonical/knowledge-library.md`.
- **D2** is SHA-256 over the exact UTF-8 bytes of `book/surprise-outerprise-examination-edition.md`.

The files are committed with LF line endings and a final newline. The verifiers read bytes; they do not parse Markdown, trim whitespace, or normalize Unicode. Therefore a one-byte change changes the corresponding digest.

Run from the repository root:

```bash
python3 scripts/verify_digests.py
a=node scripts/verify_digests.mjs
```

The scripts compare computed values to `digests/canonical-digests.json`, verify that the declared algorithm is `SHA-256`, and exit nonzero on any mismatch or missing file. The Node command above includes an accidental-safe shell variable assignment only if desired; the normal command is simply:

```bash
node scripts/verify_digests.mjs
```
