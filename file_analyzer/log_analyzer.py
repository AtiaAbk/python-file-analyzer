"""Log file analysis utilities for basic security and timeline insights."""
from typing import List, Dict, Any
import re
from collections import Counter, defaultdict
from datetime import datetime


KEYWORDS = ["error", "failed", "fail", "warning", "warn", "login"]


def analyze_log(lines: List[str]) -> Dict[str, Any]:
    """Perform log-specific analysis.

    - Count errors/warnings
    - Search for keywords
    - Detect suspicious patterns (IPs, repeated failures)
    - Basic timeline counts by hour (if timestamps present)
    """
    text = "\n".join(lines)
    lower = text.lower()

    error_count = len(re.findall(r"\berror\b", lower))
    warning_count = len(re.findall(r"\bwarn(?:ing)?\b", lower))

    keyword_counts = {k: lower.count(k) for k in KEYWORDS}

    # Detect IP addresses
    ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text)
    ip_counts = Counter(ips).most_common(20)

    # Detect repeated failed login patterns (simple heuristic)
    failed_lines = [l for l in lines if re.search(r"failed|fail|authentication", l, re.I)]
    repeated_failures = Counter(failed_lines).most_common(10)

    # Timeline analysis: try to extract ISO-like timestamps
    time_counts = defaultdict(int)
    for l in lines:
        m = re.search(r"(\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})", l)
        if m:
            try:
                dt = datetime.fromisoformat(m.group(1).replace(' ', 'T'))
                key = dt.strftime("%Y-%m-%d %H:00")
                time_counts[key] += 1
            except Exception:
                continue

    return {
        "error_count": error_count,
        "warning_count": warning_count,
        "keyword_counts": keyword_counts,
        "top_ip_counts": ip_counts,
        "repeated_failures": repeated_failures,
        "timeline_by_hour": dict(time_counts),
    }
