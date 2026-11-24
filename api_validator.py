"""Dependency-free JSON response validation helpers."""
from __future__ import annotations

from typing import Any


def validate_response(
    payload: dict[str, Any],
    required: set[str] | None = None,
    allowed_statuses: set[str] | None = None,
) -> list[dict[str, str]]:
    """Return deterministic validation signals for a JSON response."""
    signals: list[dict[str, str]] = []
    required = required or set()
    allowed_statuses = allowed_statuses or set()

    for key in sorted(required - payload.keys()):
        signals.append({
            "path": key,
            "rule": "required",
            "severity": "error",
            "message": "Required key is missing",
        })

    if allowed_statuses and "status" in payload:
        status = str(payload["status"])
        if status not in allowed_statuses:
            signals.append({
                "path": "status",
                "rule": "allowed_values",
                "severity": "error",
                "message": "Value is outside the approved set",
            })

    return signals
