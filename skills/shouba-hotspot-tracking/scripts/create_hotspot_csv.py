#!/usr/bin/env python3
"""Create an empty neutral UApiPro Xiaohongshu hotspot tracking CSV template."""
import csv
import sys
from pathlib import Path

FIELDS = [
    "fetched_at", "source", "source_url", "board_updated_at", "rank",
    "title", "heat", "original_url", "evidence_status"
]


def main():
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("shouba_hotspot_tracking.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
    print(str(output))


if __name__ == "__main__":
    main()
