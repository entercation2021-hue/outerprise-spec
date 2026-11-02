# Surprise, Outerprise — Short Draft Examination Note

**Document status:** From-scratch short draft alignment note.

**Important identification:** This file is **not** the original 105-page *Surprise, Outerprise — Examination Edition*. The original examination book is preserved at [`Surprise_Outerprise_Examination_Edition_105_Pages.pdf`](./Surprise_Outerprise_Examination_Edition_105_Pages.pdf). This Markdown file is a separate companion and must not be cited as the original book.

## Purpose

This short note tests whether an evidence-delivery system keeps separate propositions separate: that package bytes match a stated hash, that a party claims an event at a stated time, that a receiving institution records receipt, and that a Pair Key binds a sponsor identity to a project identity.

## Definitions

Let `C` denote exact package bytes and let `H(C) = SHA-256(C)` under a stated representation. Let `t_c` denote a claimed time and `t_r` denote a receiver-recorded receipt time. Let `P(sponsor, project)` denote a verified Pair Key binding. Let `A` denote a Dual Attestation recipe only when the canonical recipe and verification mechanism are actually supplied. A file hash is not `P` and is not `A`.

## Examination I — Package integrity

**Question 1.** If two parties calculate the same SHA-256 value for package bytes, what is established?

**Answer.** If both calculations used the same exact bytes, algorithm, and representation, the parties have evidence that the hash values agree for those bytes. This does not establish who created the package, whether its contents are true, when it was created, whether an institution received it, or whether a sponsor/project Pair Key exists.

**Question 2.** Does a changed Markdown line preserve the original file hash?

**Answer.** No. SHA-256 is a function of the input bytes. A changed byte produces a different hash for this protocol; any mismatch is a failure.

**Question 3.** May a verifier trim whitespace before hashing?

**Answer.** Only if the protocol explicitly defines trimming as canonicalization before hashing. Otherwise, no. The repository’s canonical artifacts are hashed as stored: UTF-8 bytes, LF line endings, and a final newline.

## Examination II — Pair Key and OPD terminology

**Question 4.** What is the exact Pair Key construction in the authoritative source?

**Answer.** The Pair Key joins a 64-character hexadecimal sponsor identity hash and a 64-character hexadecimal project identity hash. The resulting relationship identifier is 128 hexadecimal characters. The join identifies the pair; it is not a signature, password, or login.

**Question 5.** What does OPD mean?

**Answer.** OPD names the package-delivery relationship. The authoritative book records “Outer Package Delivery” on the current board and “Outerprise Package Delivery” in earlier vocabulary. This repository uses Outerprise Package Delivery as its expanded form. OPD does not mean Outerprise Proof Document.

## Examination III — Claimed time and receipt

**Question 6.** Does a sender’s timestamp prove when the receiver saw the package?

**Answer.** No. It proves, at most, that the sender asserted a time in the sender’s record. The receiver’s observation requires a separate receiver record with its own time basis.

**Question 7.** If a receiving service stores the bytes, does that validate the sender’s statement?

**Answer.** No. It may establish a storage or receipt fact if the record is authenticated and the service’s role is clear. The sender’s content claim remains a sender claim unless the receiver separately attests to it.

## Examination IV — Layer boundaries

**Question 8.** Does a Lovable interface or Supabase row constitute Entercation approval?

**Answer.** No. Integration does not transfer authority. [`TRUST.md`](../TRUST.md) keeps Supabase storage, Lovable presentation/orchestration, and Entercation operational interpretation distinct.

## Examination V — Limits of this repository

**Question 9.** What is the strongest safe conclusion from this repository’s file-hash manifest?

**Answer.** The verifier can conclude that the named committed files match their recorded SHA-256 values. It cannot conclude that the files contain every source-book proposition, that their claims are true, or that any institution received or endorsed them.

## Canonicalization and reproducibility

This short draft is a companion alignment note. The repository manifest hashes the canonical Knowledge Library compilation and the exact supplied 105-page PDF separately. Those file hashes are repository integrity checks; they do not assign a file hash the meaning of Pair Key or Dual Attestation.

## Closing note

Outerprise is strongest when it preserves distinctions: package bytes, sponsor/project identity binding, claimed time, delivery attempt, institutional receipt, and the authority of each named layer.
