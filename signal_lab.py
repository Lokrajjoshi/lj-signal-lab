"""Small, dependency-free data-quality reporting toolkit."""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


def inspect_rows(rows: list[dict[str, str]]) -> dict[str, Any]:
    columns = sorted({key for row in rows for key in row})
    missing_cells = sum(
        1 for row in rows for column in columns if not (row.get(column) or "").strip()
    )
    duplicate_rows = len(rows) - len(
        {tuple(row.get(column, "") for column in columns) for row in rows}
    )
    status_counts = dict(
        Counter((row.get("status") or "UNKNOWN").strip() or "UNKNOWN" for row in rows)
    )
    checks = len(rows) * max(len(columns), 1)
    quality_score = round(
        max(0.0, 100.0 * (1 - (missing_cells + duplicate_rows) / max(checks, 1))), 1
    )
    return {
        "rows": len(rows),
        "columns": columns,
        "missing_cells": missing_cells,
        "duplicate_rows": duplicate_rows,
        "status_counts": status_counts,
        "quality_score": quality_score,
    }


def inspect_csv(path: str | Path) -> dict[str, Any]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return inspect_rows(list(csv.DictReader(handle)))


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an explainable CSV quality report.")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    report = inspect_csv(args.csv_path)
    if args.as_json:
        print(json.dumps(report, indent=2))
        return
    print(f"Rows: {report['rows']}")
    print(f"Columns: {len(report['columns'])}")
    print(f"Quality score: {report['quality_score']}")
    print(f"Missing cells: {report['missing_cells']}")
    print(f"Duplicate rows: {report['duplicate_rows']}")
    print(f"Statuses: {report['status_counts']}")


if __name__ == "__main__":
    main()
