#!/usr/bin/env python3
"""Verify the standard UTF-8 SHA-256 test vectors published by this repository."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "test-vectors" / "sha256.json"


def main() -> int:
    data = json.loads(VECTORS.read_text(encoding="utf-8"))
    if data.get("algorithm") != "SHA-256" or data.get("encoding") != "UTF-8":
        raise SystemExit("FAIL: unexpected vector metadata")
    failures = []
    for vector in data["vectors"]:
        actual = hashlib.sha256(vector["input"].encode("utf-8")).hexdigest()
        status = "OK" if actual == vector["sha256"] else "MISMATCH"
        print(f"{vector['id']}: {status} {actual}")
        if actual != vector["sha256"]:
            failures.append(vector["id"])
    if failures:
        print("FAIL: " + ", ".join(failures))
        return 1
    print("PASS: all SHA-256 test vectors match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
