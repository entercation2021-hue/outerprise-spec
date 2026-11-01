# Integration Paradox

**Status:** Draft Knowledge Library block.

## Proposition

The more systems participate in an evidence workflow, the more carefully the workflow must separate meanings that integration tends to collapse: content identity, claimed event time, and institutional receipt.

## Formal distinction

Let `C` be a byte string, `H(C)` its SHA-256 digest, `t_c` a sender-claimed time, and `R` a receiver receipt record. The following are different predicates:

- `same(C, C')` means the byte strings are equal.
- `digest_equal(C, d)` means `H(C) = d` under the declared encoding and algorithm.
- `claimed_at(t_c)` means a party asserts an event time.
- `received(R)` means a receiver has an authenticated record containing specified receipt facts.

In general, none of these predicates implies any other one. In particular:

`digest_equal(C, d) ↛ claimed_at(t_c)` and `claimed_at(t_c) ↛ received(R)`.

## Operational consequence

An implementation should carry separate fields for the payload, digest, claimed time, sender identity, delivery attempt, receiver identity, and receipt. A UI may display them together, but the data model and verification procedure should not treat them as one assertion.

## Examination question

If two systems show the same digest, what has been established? Only that the compared digest computations agree for the specified bytes and algorithm. Truth, authorship, time, and receipt require additional evidence.
