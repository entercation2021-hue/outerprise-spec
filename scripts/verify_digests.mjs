#!/usr/bin/env node
/** Verify the repository's canonical artifact file-hash manifest. */
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const manifestPath = resolve(root, "digests/canonical-digests.json");
const manifest = JSON.parse(readFileSync(manifestPath, "utf8"));

if (manifest.algorithm !== "SHA-256") {
  console.error("FAIL: manifest algorithm is not SHA-256");
  process.exit(1);
}
if (!manifest.scope?.startsWith("repository file integrity")) {
  console.error("FAIL: manifest scope is not repository file integrity");
  process.exit(1);
}

const failures = [];
for (const [name, item] of Object.entries(manifest.file_hashes)) {
  const path = resolve(root, item.path);
  const actual = createHash("sha256").update(readFileSync(path)).digest("hex");
  const status = actual === item.sha256 ? "OK" : "MISMATCH";
  console.log(`${name}: ${status} ${actual}  ${item.path}`);
  if (actual !== item.sha256) failures.push(name);
}

if (failures.length) {
  console.error(`FAIL: ${failures.join(", ")}`);
  process.exit(1);
}
console.log("PASS: all repository file hashes match");
