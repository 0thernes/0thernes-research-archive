#!/usr/bin/env python3
"""Validate one or more formalization.yaml files against the official Palomar Registry v0.4 JSON Schema.

Checks:
  1. Valid UTF-8 YAML mapping with version == "v0.4"
  2. Full Draft-07 JSON Schema validation against schema/palomar-v0.4.schema.json
  3. Zero leftover "TEMPLATE" sentinel strings
  4. Non-empty classification (arxiv/msc2020) and Apache-2.0/MIT SPDX license notice

Usage:
    python scripts/validate_palomar_v04.py path/to/formalization.yaml [...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "palomar-v0.4.schema.json"


def find_templates(obj: Any, path: str = "$") -> list[str]:
    hits: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            hits.extend(find_templates(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits.extend(find_templates(v, f"{path}[{i}]"))
    elif isinstance(obj, str) and obj.lstrip().startswith("TEMPLATE"):
        hits.append(path)
    return hits


def validate_file(yaml_path: Path, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"YAML parse error: {exc}"]
    if not isinstance(doc, dict):
        return ["Top-level document must be a YAML mapping"]
    if doc.get("version") != "v0.4":
        errors.append(f"$.version must be 'v0.4' for Palomar Registry Gate 3, got {doc.get('version')!r}")
    v = jsonschema.Draft7Validator(schema)
    for err in sorted(v.iter_errors(doc), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in err.path) or "$"
        errors.append(f"schema[{loc}]: {err.message}")
    for tp in find_templates(doc):
        errors.append(f"leftover TEMPLATE sentinel at {tp}")
    return errors


def main(argv: list[str]) -> int:
    if not argv:
        print("Usage: python scripts/validate_palomar_v04.py <formalization.yaml> [...]")
        return 2
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    failed = 0
    for arg in argv:
        p = Path(arg)
        errs = validate_file(p, schema)
        if errs:
            failed += 1
            print(f"FAIL {p} ({len(errs)} error(s)):")
            for e in errs[:12]:
                print(f"  - {e}")
        else:
            print(f"PASS {p} (valid Palomar formalization.yaml v0.4)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
