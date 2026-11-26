#!/usr/bin/env python3
"""Re-seal data/RELEASE_FREEZE.sha256 with an RFC 3161 timestamp (one command).

Run this after any change to a file covered by the release freeze (registry JSON, archived
papers and artifacts), then `python scripts/verify_archive.py`.

What leaves the machine: only the SHA-256 digest of data/RELEASE_FREEZE.sha256, inside a
standard RFC 3161 TimeStampReq built by `openssl ts -query`. The default authority is
DigiCert's public TSA (no account, no key). The previous token stays in git history, so every
re-seal is itself auditable.

Usage:
    python scripts/stamp_freeze.py                 # stamp, check the reply, write the .tsr
    python scripts/stamp_freeze.py --tsa URL       # use another RFC 3161 authority
    python scripts/stamp_freeze.py --dry-run       # build the request only
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FREEZE = ROOT / "data" / "RELEASE_FREEZE.sha256"
TSR = ROOT / "data" / "RELEASE_FREEZE.sha256.tsr"
DEFAULT_TSA = "http://timestamp.digicert.com"


def openssl() -> str:
    exe = shutil.which("openssl")
    if not exe:
        raise SystemExit("openssl not found on PATH (Git for Windows ships one under usr/bin)")
    return exe


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tsa", default=DEFAULT_TSA)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    digest = hashlib.sha256(FREEZE.read_bytes()).digest()
    with tempfile.TemporaryDirectory() as tmp:
        tsq = Path(tmp) / "freeze.tsq"
        subprocess.run(
            [openssl(), "ts", "-query", "-data", str(FREEZE), "-sha256", "-cert", "-out", str(tsq)],
            check=True, capture_output=True,
        )
        if args.dry_run:
            print(f"request built ({tsq.stat().st_size} bytes) for SHA-256 {digest.hex()}")
            return 0
        req = urllib.request.Request(
            args.tsa, data=tsq.read_bytes(), headers={"Content-Type": "application/timestamp-query"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310 (fixed public TSA URL)
            reply = resp.read()
        new_tsr = Path(tmp) / "freeze.tsr"
        new_tsr.write_bytes(reply)
        text = subprocess.run(
            [openssl(), "ts", "-reply", "-in", str(new_tsr), "-text"],
            check=True, capture_output=True, text=True,
        ).stdout
        if "Status: Granted" not in text:
            print(text)
            raise SystemExit("TSA did not grant the timestamp; the old token was kept")
        if digest not in reply:
            raise SystemExit("TSA reply does not embed the freeze digest; the old token was kept")
        TSR.write_bytes(reply)
        when = next((ln.split(":", 1)[1].strip() for ln in text.splitlines() if ln.startswith("Time stamp:")), "?")
        print(f"PASS: {TSR.relative_to(ROOT).as_posix()} sealed at {when} by {args.tsa} "
              f"for SHA-256 {digest.hex()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
