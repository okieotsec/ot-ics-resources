# SPDX-License-Identifier: MIT
"""Validate structure, cost classification, dates and publishing counts."""
import argparse
import sys
from catalog import load, validate

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--catalog", help="Alternate JSON file, useful for reviewing changes.")
    args = p.parse_args()
    try:
        data = load(args.catalog)
    except (OSError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    errors, warnings = validate(data)
    for w in warnings:
        print("NOTE:", w)
    for e in errors:
        print("ERROR:", e, file=sys.stderr)
    if errors:
        return 1
    print("Catalog valid:", data["counts"])
    return 0

if __name__ == "__main__":
    sys.exit(main())
