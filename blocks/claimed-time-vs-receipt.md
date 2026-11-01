# Claimed Time vs. Institutional Receipt

**Status:** Draft Knowledge Library block.

## Two clocks, two assertions

A sender may assert `t_c`, the time at which it created, signed, or dispatched a statement. A receiving institution may record `t_r`, the time at which its system accepted or logged a delivery. These values can differ because of delay, clock skew, retries, batching, or later reconciliation.

The safe representation is:

```text
claimed_time: { value: t_c, asserted_by: sender, basis: stated_basis }
receipt_time: { value: t_r, recorded_by: receiver, basis: receiver_record }
```

Neither value should be relabeled as the other. If a timezone, clock source, precision, or synchronization status is unknown, that limitation belongs in the record.

## Mathematical note

The ordering `t_c ≤ t_r` may be expected operationally, but it is not a theorem of the data model. Without a trusted time basis and authenticated clocks, a verifier can compare the values but cannot infer their real-world accuracy from the comparison alone.

## Practical rule

Report sender time as claimed time and receiver time as receipt time. Do not use a single “timestamp” field where the distinction matters.
