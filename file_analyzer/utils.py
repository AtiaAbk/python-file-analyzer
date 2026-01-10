"""Utility helpers for printing and small helpers."""
from typing import Any, Dict
import json


def print_summary(summary: Dict[str, Any]) -> None:
    """Print a JSON-formatted summary in a readable way."""
    print(json.dumps(summary, indent=2, default=str))
