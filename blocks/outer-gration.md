# Outer-Gration

**Status:** Draft Knowledge Library block.

## Definition

Outer-Gration is the controlled movement of an evidence artifact from an originating operational context to an external receiving context. It is a boundary operation, not an assertion that the two contexts share authority.

## Boundary record

A useful boundary record contains:

1. the exact artifact or a resolvable artifact reference;
2. the artifact digest and algorithm;
3. the originator and the sender’s role;
4. the delivery channel and attempt identifier;
5. any sender-claimed time;
6. a receiver-generated receipt, if one exists; and
7. limitations, transformations, and unresolved conditions.

## Failure semantics

“Sent,” “delivered,” “opened,” “accepted,” and “acted upon” are distinct statuses. A system must not promote one status to the next without evidence for the additional transition. A retry may create a new delivery attempt while preserving the same content digest.

## Examination question

If the external recipient stores a copy, what is newly established? At most, the receiver’s storage or receipt fact, subject to authentication and the receiver’s own record. The sender’s content claims remain sender claims.
