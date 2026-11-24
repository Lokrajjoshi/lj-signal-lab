# API Validation Plan

The next LJ Signal Lab adapter will accept JSON responses from internal or public APIs and report:

- missing required keys
- unexpected fields
- type mismatches
- invalid status values
- response-shape drift

The adapter should stay dependency-free at first. Each rule will return a structured signal with:

```json
{
  "path": "project.status",
  "rule": "allowed_values",
  "severity": "error",
  "message": "Value is outside the approved set"
}
```

## Delivery sequence

1. Define a small JSON fixture set.
2. Implement deterministic validation rules.
3. Add unit tests for valid, invalid, and missing fields.
4. Export machine-readable results for reporting workflows.
5. Add the adapter to the quality gate.

This keeps API testing aligned with the project's analyst-first and quality-engineering focus.
