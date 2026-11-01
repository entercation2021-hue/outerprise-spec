# Pair Key / Dual Attestation

**Status:** Draft alignment block.

## Established meaning

In the Outerprise architecture, a **Pair Key** binds a sponsor identity to a project identity. It is an identity-and-scope binding, not a sender/receiver receipt object and not a replacement for the canonical Dual Attestation recipes.

The binding answers the narrower question: “Which sponsor and which project are paired for this Outerprise surface?” It must not be expanded into a claim that content is true, that a delivery was received, or that a platform endorsed the project.

## Scope boundary

A Pair Key may be referenced by an attestation or delivery record, but the reference does not change the meaning of either record. Content integrity, claimed time, delivery attempt, institutional receipt, and sponsor/project identity binding remain separate fields and separate propositions.

The original canonical Dual Attestation recipes are not present in this workspace. This draft therefore does not invent their field names, key material, or verification equations. A future canonical export should replace this alignment block with the established recipes verbatim.

## Non-inheritance

A sponsor/project binding does not inherit authority from Supabase storage, Lovable presentation, Entercation operations, or a receiving institution. Conversely, a receipt or content digest does not establish the sponsor/project pairing unless the relevant Pair Key binding is independently present and verified.

## Examination rule

Do not use the retired sender/receiver interpretation for Pair Key. The established scope is sponsor/project identity binding.
