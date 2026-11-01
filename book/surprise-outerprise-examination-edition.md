# Surprise, Outerprise — Examination Edition

**Status:** From-scratch draft implementation note.

## Abstract

This examination edition tests whether an evidence-delivery system keeps three propositions separate: that content is identical to a digest, that a party claims an event at a stated time, and that an institution records receipt. The central discipline is non-inheritance: evidence at one layer does not silently become authority at another layer.

## Definitions

Let `C` denote an exact byte string and let `H(C) = SHA-256(C)`. Let `t_c` denote a sender-claimed time and `t_r` denote a receiver-recorded receipt time. Let `A_s` be a sender attestation and `A_r` be a receiver attestation. A verification result is valid only within the scope of the algorithm, encoding, identity mechanism, and receipt record it names.

## Examination I — Content integrity

**Question 1.** If two parties calculate the same SHA-256 value for an artifact, what is established?

**Answer.** If both calculations used the same exact bytes, algorithm, and representation, the parties have evidence that the digest values agree for those bytes. This does not establish who created the artifact, whether its contents are true, when it was created, or whether an institution received it.

**Question 2.** Does a changed Markdown line preserve the original digest?

**Answer.** No. SHA-256 is a function of the input bytes. A changed byte normally produces a different digest; for this protocol, any mismatch is treated as a failure rather than relying on probabilistic language.

**Question 3.** May a verifier trim whitespace before hashing?

**Answer.** Only if the protocol explicitly defines trimming as canonicalization before hashing. Otherwise, no. The canonical artifacts in this repository are hashed as stored: UTF-8 bytes, LF line endings, and a final newline.

## Examination II — Claimed time

**Question 4.** Does a sender’s timestamp prove when the receiver saw the artifact?

**Answer.** No. It proves, at most, that the sender asserted a time in the sender’s record. The receiver’s observation requires a separate receiver record with its own time basis.

**Question 5.** Is `t_c ≤ t_r` guaranteed by the field names?

**Answer.** No. The data model permits comparison but does not supply synchronized clocks, trusted time sources, or authenticated event ordering. A protocol may reject implausible values operationally, but rejection is not proof of real-world time accuracy.

## Examination III — Receipt and authority

**Question 6.** If a receiving service stores the bytes, does that validate the sender’s statement?

**Answer.** No. It may establish a storage or receipt fact if the record is authenticated and the service’s role is clear. The sender’s content claim remains a sender claim unless the receiver separately attests to it.

**Question 7.** Does a Lovable interface or Supabase row constitute Entercation approval?

**Answer.** No. Integration does not transfer authority. The three-layer carve-out in [`TRUST.md`](../TRUST.md) keeps Supabase storage, Lovable presentation/orchestration, and Entercation operational interpretation distinct.

## Examination IV — Pair key

**Question 8.** What does dual attestation add?

**Answer.** It makes two roles explicit: a content attestor and a receipt attestor. The verifier checks each attestation under its stated mechanism and confirms both bind to the same digest. It does not turn two unsupported statements into truth; it makes their provenance and scope inspectable.

**Question 9.** What happens after transformation?

**Answer.** The transformed bytes are a new artifact with a new digest. The provenance record should identify the transformation and preserve the predecessor digest if the relationship matters.

## Examination V — Protocol limits

**Question 10.** What is the strongest safe conclusion from a verified OPD with no receiver receipt?

**Answer.** The verifier may conclude that the OPD’s specified content digest matches the available bytes and that any authenticated sender claim passed its stated check. The verifier should report institutional receipt as not established.

## Model conclusion

A careful report should say: “The available bytes match digest `d` under SHA-256 and the declared UTF-8 representation. The sender claimed event time `t_c`. No receiver receipt was provided, or the receipt was verified at `t_r` under the stated mechanism. These findings do not establish truth, authorship beyond the attestation mechanism, or institutional action beyond the recorded receipt.”

## Canonicalization and reproducibility

This book is D2 input. It is hashed as exact UTF-8 bytes with LF line endings and a final newline. The companion manifest records the SHA-256 value. The Python and Node.js scripts read bytes without trimming or Unicode normalization.

## Closing note

Outerprise is strongest when it is modest: preserve the artifact, name the claimant, separate the clocks, bind receipts to digests, state the layer making each claim, and expose what remains unknown.
