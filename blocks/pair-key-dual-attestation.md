# Pair Key / Dual Attestation

**Status:** Draft alignment block.

## Established meaning

In the Outerprise architecture, a **Pair Key** identifies one sponsor and one project together. It is formed by joining the sponsor identity hash and the project identity hash:

```text
pair_key = sponsor_identity_hash || project_identity_hash
```

Each identity hash is a 64-character hexadecimal value. The resulting Pair Key is a 128-character hexadecimal relationship identifier. The join is an identity binding; it is not a new signature, password, login, or proof that funds were received.

## Scope boundary

A Pair Key may be referenced by an attestation or delivery record, but the reference does not change the meaning of either record. Content integrity, claimed time, delivery attempt, institutional receipt, and sponsor/project identity binding remain separate fields and separate propositions.

The authoritative examination book contains the paired-identity definition. Any separate canonical Dual Attestation recipe must be cited at its own source location and must not be inferred from the Pair Key’s 128-character identity join.

## Non-inheritance

A sponsor/project binding does not inherit authority from Supabase storage, Lovable presentation, Entercation operations, or a receiving institution. Conversely, a receipt or content digest does not establish the sponsor/project pairing unless the relevant Pair Key binding is independently present and verified.

## Examination rule

Do not use the retired sender/receiver interpretation for Pair Key. The established scope is the concatenation of the sponsor and project identity hashes.
