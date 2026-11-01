#!/usr/bin/env python3
"""Verify the canonical Outerprise SHA-256 digest manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "digests" / "canonical-digests.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("algorithm") != "SHA-256":
        raise SystemExit("FAIL: manifest algorithm is not SHA-256")

    failures = []
    for name, item in manifest["digests"].items():
        path = ROOT / item["path"]
        actual = sha256_file(path)
        expected = item["sha256"]
        status = "OK" if actual == expected else "MISMATCH"
        print(f"{name}: {status} {actual}  {item['path']}")
        if actual != expected:
            failures.append(name)

    if failures:
        print("FAIL: " + ", ".join(failures))
        return 1
    print("PASS: all canonical digests match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
