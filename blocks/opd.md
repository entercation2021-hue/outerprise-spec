# OPD — Outerprise Package Delivery

**Status:** Draft alignment block.

## Established meaning

OPD means **Outerprise Package Delivery**. It describes the delivery of an Outerprise package across a defined boundary. It is not an “Outerprise Proof Document,” and the acronym must not be expanded that way in examination materials.

An OPD may carry evidence fields, package references, integrity hashes, claimed times, delivery attempts, and receipt data. Those fields describe the package and its delivery; they do not manufacture proof or transfer authority between layers.

## Required conceptual separation

```text
package_reference
package_integrity_hash { algorithm, value, encoding }
pair_key_reference
claimed_time { value, timezone, precision, basis }
delivery { channel, attempt_id, sent_at }
receipt { status, receiver, received_at, evidence_reference }
provenance { producer, transformations[] }
limitations[]
```

A field may be `unknown`, `not asserted`, or `not available`; omission must not be interpreted as confirmation. The `pair_key_reference` identifies the relevant sponsor/project binding when one is present. It does not turn the OPD into the Pair Key itself.

## Integrity rule

For package bytes `C`, calculate `d = SHA-256(C)` only when the byte representation, encoding, and algorithm are specified. If a package is transformed, the transformed bytes have a new hash unless the bytes are exactly unchanged.

## Boundary rule

An OPD can make package delivery inspectable. It cannot turn an unsupported claim into a fact, establish institutional receipt without a receiver record, or transfer institutional authority from one named layer to another.
