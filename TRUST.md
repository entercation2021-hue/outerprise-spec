# Trust boundaries and non-inheritance

This draft uses a three-layer carve-out:

1. **Supabase layer — storage and persistence.** Supabase may store bytes, rows, metadata, and database timestamps according to the configured service and application behavior. Storage does not, by itself, attest that a submitted statement is true or that a human institution received it.
2. **Lovable layer — application presentation and orchestration.** Lovable may render interfaces or orchestrate application behavior as configured. An interface, workflow, or generated response does not, by itself, become an institutional attestation.
3. **Entercation layer — operational interpretation and delivery practice.** Entercation may define the evidence envelope, operational procedures, review process, and delivery handoff. Entercation statements are not automatically statements of Supabase or Lovable.

## Non-inheritance language

No claim, timestamp, signature, digest, workflow status, database row, user-interface display, or delivery event inherits authority from another layer merely because the layers are integrated. Authority, provenance, and receipt must be stated and evidenced at the layer that makes the relevant claim.

In particular:

- A content digest establishes byte equality for the specified artifact; it does not establish truth, authorship, or institutional receipt.
- A sender’s claimed timestamp establishes only that the sender made that claim in the stated format; it does not establish when a receiver saw or accepted the content.
- A receiving system’s receipt establishes only the receipt facts it actually records and can authenticate; it does not retroactively validate the content’s truth.
- A platform’s storage or rendering of an artifact does not constitute endorsement by the platform, its operator, or any other layer.

This document is a draft implementation note and does not create a contractual warranty, legal notice, or audit conclusion.
