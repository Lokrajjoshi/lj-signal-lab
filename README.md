# LJ Signal Lab

Evidence-first data quality and workflow validation for analyst-minded engineers.

Turn a CSV into a small, explainable quality report:

- missing-value signals
- duplicate-record signals
- status distribution
- transparent quality scoring
- machine-readable JSON output

## Why it exists

Business and technical decisions are only as reliable as the data behind them. LJ Signal Lab provides a dependency-free starting point for inspecting workflow data before it reaches a dashboard, report, or operational decision.

```
CSV input → validation rules → quality signals → decision-ready report
```

## Quick start

```bash
python signal_lab.py data/example_projects.csv --json
```

## Validation signals

| Signal | Meaning |
| --- | --- |
| Missing cells | Fields that need completion before analysis |
| Duplicate rows | Potential repeated records or ingestion issues |
| Status distribution | Operational flow visibility |
| Quality score | Transparent summary of observed data health |

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project map

- `signal_lab.py` — reusable CSV inspection engine and CLI
- `data/example_projects.csv` — small project-tracking sample
- `tests/test_signal_lab.py` — regression tests for quality signals

## Roadmap

- configurable validation rules
- SQL adapter for warehouse extracts
- API response validator
- HTML report export
- dashboard-ready JSON schema

Built for Data & Business Analysis · Technical Solutions · Quality Engineering.
