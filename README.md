# Outerprise specification surface

External Evidence Delivery: Separating Content Integrity, Claimed Time, and Institutional Receipt. An Entercation implementation note.

This repository is a draft examination surface for the Outerprise evidence-delivery model. It distinguishes what can be checked cryptographically from what is asserted by a participant, acknowledged by a recipient, or recorded as a sponsor/project relationship.

## Start here

- [Entercation ecosystem and live-app entry points](https://github.com/entercation2021-hue/Entercation-AI-Frameworks)
- [Micro and Macro receipts](./blocks/micro-macro-receipts.md)
- [Outerprise and enterprise integration comparison](https://doi.org/10.5281/zenodo.24305668)
- [Knowledge Library index](./index.md)

[**Open OIGP v1.3.1: Cryptographic Fiscal Sponsorship State Machine**](https://doi.org/10.5281/zenodo.24177899)

Follow the approved and denied synthetic draws through sponsor decision, payment evidence, and closeout. The walkthrough shows how a reviewer can examine the supplied records without a standing connection to the system that produced them. Use the instructions in the versioned OIGP archive to reproduce its checks.

## Publications and worked examples

- [Outerprise Waste Metric report and publication guide](https://doi.org/10.5281/zenodo.24182132): a worksheet for comparing the cost of equivalent reviews. It does not establish measured savings.
- [Data Center Transparency](https://doi.org/10.5281/zenodo.23993510): synthetic disclosures and the limits of what their evidence establishes.
- [Outerprise specification surface](https://doi.org/10.5281/zenodo.23873552): Entercation Info Inc.’s draft specification for integrity, claimed time, and institutional receipt.

[Live app](https://entercation.lovable.app/) · [Knowledge Library](https://outerprise-knowledge-library.lovable.app/) · [Vince Jones on ORCID](https://orcid.org/0009-0008-6712-8136)

## Repository materials

- [Trust and non-inheritance statement](./TRUST.md)
- [Canonical Knowledge Library compilation](./canonical/knowledge-library.md)
- [Surprise, Outerprise — 105-page Examination Edition PDF](./book/Surprise_Outerprise_Examination_Edition_105_Pages.pdf)
- [Short draft alignment note](./book/surprise-outerprise-examination-edition.md)
- [Repository file-hash manifest](./digests/canonical-digests.json)
- [Verification scripts](./scripts/)
- [Citation metadata](./CITATION.cff)
- [MIT License](./LICENSE)

## Scope and status

These materials are draft specifications and worked examples. They do not establish an audit opinion, regulatory approval, or acceptance by any named institution. A matching digest supports an integrity check against a trusted reference; it does not by itself establish authorship, truth, creation time, delivery, or receipt.

The 105-page Examination Edition PDF is the authoritative book artifact in this repository. The short Markdown alignment note is a separate companion and should not be cited as the book.

OPD names the package-delivery relationship. The book records **Outer Package Delivery** on the current board and **Outerprise Package Delivery** in earlier vocabulary; this repository uses the latter expansion. In this specification, the Pair Key concatenates a 64-hex sponsor identity hash and a 64-hex project identity hash into a 128-hex relationship identifier. It is not a signature, password, or login.

## Verify this repository

The repository manifest records SHA-256 hashes of exact file bytes. These are repository integrity checks, separate from Pair Key values, Dual Attestation recipes, and institutional receipts. Run these commands from the repository root:

```bash
python3 scripts/verify_digests.py
node scripts/verify_digests.mjs
python3 scripts/verify_test_vectors.py
```

## Internet-Drafts and archival copies

Each row links a fixed Internet-Draft revision and its Zenodo citation. Internet-Drafts are works in progress.

| Internet-Draft revision | Zenodo archive |
| --- | --- |
| [MiMS Reproducible Draft Review (00)](https://www.ietf.org/archive/id/draft-jones-mims-reproducible-draft-review-00.html) | [10.5281/zenodo.24450421](https://doi.org/10.5281/zenodo.24450421) |
| [SCITT Dual-Receipt Profile (02)](https://www.ietf.org/archive/id/draft-jones-scitt-dual-receipt-02.html) | [10.5281/zenodo.24415155](https://doi.org/10.5281/zenodo.24415155) |
| [Detached Evidence Handoffs (03)](https://www.ietf.org/archive/id/draft-jones-detached-evidence-handoffs-03.html) | [10.5281/zenodo.24415158](https://doi.org/10.5281/zenodo.24415158) |
| [Detached Evidence Examination (00)](https://www.ietf.org/archive/id/draft-jones-detached-evidence-examination-00.html) | [10.5281/zenodo.24415162](https://doi.org/10.5281/zenodo.24415162) |
| [Outerprise Visual Manual (00)](https://www.ietf.org/archive/id/draft-jones-outerprise-visual-manual-00.html) | [10.5281/zenodo.24415152](https://doi.org/10.5281/zenodo.24415152) |
| [Outerprise Four-Gate Onboarding (00)](https://www.ietf.org/archive/id/draft-jones-outerprise-four-gate-onboarding-00.html) | [10.5281/zenodo.24415135](https://doi.org/10.5281/zenodo.24415135) |

For the worked fiscal sponsorship example, cite the OIGP version used for verification. [OIGP v1.3.4](https://doi.org/10.5281/zenodo.24197013) · [OIGP v1.3.1](https://doi.org/10.5281/zenodo.24177899)
