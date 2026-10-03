#!/usr/bin/env python3
"""Validate channels.json against the Simorgh channel registry schema.

Schema: a JSON array where every entry has exactly the keys
  id       — unique short name (string)
  name     — display name (string)
  url      — public web preview URL, https://t.me/s/<id> (string)
  tier     — 1 priority (read every 10 min), 2 directory, 3 general (int)
  language — BCP-47 primary tag, e.g. "fa" (string)

Written for the channels-lint workflow; exit code 0 = valid.
"""
import json
import sys

REQUIRED_KEYS = {"id", "name", "url", "tier", "language"}
VALID_TIERS = {1, 2, 3}


def fail(msg: str) -> None:
    print(f"INVALID: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "channels.json"
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        fail(f"{path}: not valid JSON: {exc}")
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")

    if not isinstance(data, list):
        fail("top level must be an array")

    ids = set()
    for i, entry in enumerate(data):
        where = f"entry {i} ({entry.get('id', '?') if isinstance(entry, dict) else '?'})"
        if not isinstance(entry, dict):
            fail(f"{where}: not an object")
        keys = set(entry)
        if keys != REQUIRED_KEYS:
            missing = REQUIRED_KEYS - keys
            extra = keys - REQUIRED_KEYS
            if missing:
                fail(f"{where}: missing keys {sorted(missing)}")
            if extra:
                fail(f"{where}: unexpected keys {sorted(extra)}")
        for key in ("id", "name", "url", "language"):
            if not isinstance(entry[key], str) or not entry[key]:
                fail(f"{where}: {key} must be a non-empty string")
        if not isinstance(entry["tier"], int) or isinstance(entry["tier"], bool):
            fail(f"{where}: tier must be an integer")
        if entry["tier"] not in VALID_TIERS:
            fail(f"{where}: tier {entry['tier']} not in {sorted(VALID_TIERS)}")
        if not entry["url"].startswith("https://t.me/"):
            fail(f"{where}: url must start with https://t.me/")
        if entry["id"] in ids:
            fail(f"{where}: duplicate id {entry['id']!r}")
        ids.add(entry["id"])

    print(f"OK: {path} — {len(data)} channels, schema valid")


if __name__ == "__main__":
    main()
