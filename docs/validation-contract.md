# Validation Contract

LJ Signal Lab treats validation as an explainable contract between raw workflow data and a decision.

## Checks

| Check | Rule | Why it matters |
| --- | --- | --- |
| Required fields | Empty values are reported as missing cells | Prevents incomplete records from silently reaching reports |
| Duplicate rows | Identical records are counted once as a duplicate signal | Surfaces ingestion or copy/paste issues |
| Status values | Missing statuses are normalized to `UNKNOWN` | Keeps operational summaries consistent |
| Quality score | Starts at 100 and decreases from observed signals | Gives stakeholders a transparent comparison point |

## Extension path

New checks should:

1. Produce a deterministic value.
2. Be covered by a regression test.
3. Be described in the README.
4. Preserve the dependency-free CLI.

This keeps analysis reproducible for analysts, engineers, and reviewers.
