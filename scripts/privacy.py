#!/usr/bin/env python3
"""Privacy firewall that does not name what it protects.

PRIVATE_SHA256 holds SHA-256 digests of the lower-cased names of the owner's non-public
GitHub repositories. Storing digests instead of names keeps those names out of this public
repository while still letting every check reject them. The digests are a second line of
defence: scripts/live_sync.py also rejects any repository that the GitHub API reports as
private or as a fork.

Refresh the list (needs the authenticated gh CLI; prints digests only, never names):
    python scripts/privacy.py --refresh
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys

OWNER = "0thernes"
_TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")

PRIVATE_SHA256: frozenset[str] = frozenset(
    {
    "079948af399b77926df95165762cdc3adec1fe35e829e81b44ef5027f3429e27",
    "2a1742c3fd702f5ea7f7e663f6480008ad474dea0557c6291168f271fb3c56d9",
    "2dcb95d928b1fe91ab202b1db8010ed1dd635b6b59c372aa29242a222ce4843b",
    "3948d099ac20f2305f0b5b50637ef35a81fd590b24b472c8ac88da5d5235ed0b",
    "39b884fd4faf904a017eab34a1418af462af4a8c33c1f72caec545c39c71d7f7",
    "408fdb8a250f187117f30f4a9b6134cd901383a0b6c3d7669e22e39eb2c62688",
    "50a590684b46558dea51cdca0838d4ae9c50656f449f07fe03c4cfbb93098693",
    "6c043b42afca0012965d2b7e9287cb276ab242ea214028b383ef77759e448c55",
    "87e72566c7a8cacea344d8bf821b968c6ff0bd623ef4c0ccd430adfb9e15f5d0",
    "aac98619a22e4758838386ba5251c1ae3b31089c14c576114f647239a244d121",
    "b4e8d63bb04ffdc6251e6304dccf19ca7480d26cc1c7ebbea5891d223b6d44f1",
    "bd8e2025e644fcee759b8cb5c879c85cf29eee4c7a8076696a572fc6de96ddd4",
    "c0e22594b265289a6443fcec7245121cda584d6899fa94779922695fac531516",
    "fb984795804f34af19c8f8c67641d476bf1dd2fc36ccb659ba31826fc9a60606",
    }
)


def digest(name: str) -> str:
    """SHA-256 of a repository name as GitHub compares it (case-insensitive)."""
    return hashlib.sha256(name.strip().lower().encode("utf-8")).hexdigest()


def is_private_name(name: str, digests: frozenset[str] | None = None) -> bool:
    """True if name is a non-public repository (digests default to PRIVATE_SHA256, read at call time)."""
    return digest(name) in (PRIVATE_SHA256 if digests is None else digests)


def private_names_in(text: str, digests: frozenset[str] | None = None) -> list[str]:
    """Every token of text that is the name of a non-public repository (empty list = clean)."""
    pool = PRIVATE_SHA256 if digests is None else digests
    return sorted({tok for tok in _TOKEN.findall(text) if digest(tok) in pool})


def refresh() -> int:
    res = subprocess.run(
        ["gh", "repo", "list", OWNER, "--limit", "1000", "--json", "name,visibility"],
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if res.returncode != 0:
        print("gh repo list failed:", res.stderr.strip())
        return 1
    names = [r["name"] for r in json.loads(res.stdout) if r.get("visibility") != "PUBLIC"]
    for h in sorted(digest(n) for n in names):
        print(f'        "{h}",')
    print(f"# {len(names)} non-public repositories; paste the lines above into PRIVATE_SHA256.")
    return 0


if __name__ == "__main__":
    sys.exit(refresh() if "--refresh" in sys.argv else 0)
