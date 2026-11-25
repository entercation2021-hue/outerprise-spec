"""Offline checks for the pinned, synthetic Appendix A examples."""
import hashlib
import json
from pathlib import Path

data = json.loads(Path(__file__).with_name("test-vectors.json").read_text())
vectors = {v["id"]: v["expected_hex"] for v in data["suites"][0]["vectors"]}
results = []

def H(value):
    return hashlib.sha256(value).digest()

def Hd(label, value):
    return H(b"outerprise-resolutions/v1/" + label.encode("ascii") + b"\0" + value)

def fixture_json(value):
    # Pinned fixtures use ASCII keys/strings and small integers only.
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("ascii")

def check(vector, label, value):
    expected = vectors[vector][label]
    observed = value.hex()
    results.append({"vector":vector,"assertion":label,"expected":expected,"observed":observed,"result":"MATCH" if expected==observed else "MISMATCH"})

def cbor_bytes(value):
    size = len(value)
    assert size <= 255
    return (bytes([0x40+size]) if size < 24 else bytes([0x58,size])) + value

sids = []
for i in range(1,5):
    statement = {"iss":"demo-issuer-1","seq":i,"statement":"demo-supply-chain-event","sub":"demo-artifact-1","v":1}
    sid = Hd("statement",fixture_json(statement))
    sids.append(sid)
    check("V1",f"SID[{i}]",sid)
    if i==1:
        check("V2","SID",Hd("statement",fixture_json(dict(reversed(list(statement.items()))))))

leaves=[Hd("leaf",s) for s in sids]
leaf_hashes=[H(b"\0"+leaf) for leaf in leaves]
for i,(leaf,lh) in enumerate(zip(leaves,leaf_hashes),1):
    check("V3",f"LEAF[{i}]",leaf)
    check("V3",f"leaf hash[{i}]",lh)
nodes=[H(b"\1"+leaf_hashes[i]+leaf_hashes[i+1]) for i in [0,2]]
check("V3","node[1..2]",nodes[0])
check("V3","node[3..4]",nodes[1])
root=H(b"\1"+b"".join(nodes))
check("V3","root",root)

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
v4=vectors["V4"]
key=Ed25519PrivateKey.from_private_bytes(bytes.fromhex(v4["test seed (Ed25519 private key)"]))
public=key.public_key()
header=bytes.fromhex("a10132")
payload=fixture_json({"root":root.hex(),"tree_size":4})
sig_input=b"\x84\x6aSignature1"+cbor_bytes(header)+b"\x40"+cbor_bytes(payload)
signature=key.sign(sig_input)
check("V4","Sig_structure (108 octets)",sig_input)
check("V4","SHA-256(Sig_structure)",H(sig_input))
check("V4","public key",public.public_bytes(Encoding.Raw,PublicFormat.Raw))
check("V4","signature",signature)
check("V4","COSE_Sign1, tag 18 (164 octets)",b"\xd2\x84"+cbor_bytes(header)+b"\xa0"+cbor_bytes(payload)+cbor_bytes(signature))
public.verify(signature,sig_input)
for label, value in [
    ("changed payload byte",sig_input[:-1]+b"]"),
    ("CBOR byte-string context",sig_input[:1]+b"\x4a"+sig_input[2:]),
    ("changed tree size",sig_input[:-2]+b"5}")]:
    observed="ACCEPTED"
    try: public.verify(signature,value)
    except InvalidSignature: observed="REJECTED"
    results.append({"vector":"V4","assertion":label,"expected":"REJECTED","observed":observed,"result":"MATCH" if observed=="REJECTED" else "MISMATCH"})

v5=vectors["V5"]
d1,d2=(bytes.fromhex(v5[k]) for k in ("D1","D2"))
check("V5","CID = SHA-256(D1 || D2)",H(d1+d2))
check("V5","Negative, SHA-256(D2 || D1)",H(d2+d1))
check("V5","Negative, SHA-256 over the 128-character hex text",H((d1+d2).hex().encode("ascii")))
check("V6",'Hd("payload", payload)',Hd("payload",b"demo-payload-bytes-for-detached-evidence"))
for label,domain in [("binding",b"demo-verifier.example"),('Negative, domain "other-verifier.example"',b"other-verifier.example")]:
    check("V7",label,Hd("presentation",b"demo-challenge-7f3a\0"+domain+b"\0"+sids[0]))
print(json.dumps(results,indent=2))
raise SystemExit(any(r["result"]!="MATCH" for r in results))
