"""Core text file analysis utilities."""
from typing import List, Dict, Tuple
import os
import re
from collections import Counter


def read_file(path: str) -> List[str]:
    """Read a file safely and return list of lines.

    Raises FileNotFoundError or PermissionError for callers to handle.
    """
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()


def get_metadata(path: str, lines: List[str]) -> Dict[str, int]:
    """Return basic metadata for the file."""
    try:
        size = os.path.getsize(path)
    except OSError:
        size = -1
    words = sum(len(re.findall(r"\S+", line)) for line in lines)
    chars = sum(len(line) for line in lines)
    return {
        "size_bytes": size,
        "num_lines": len(lines),
        "num_words": words,
        "num_chars": chars,
    }


def analyze_text(lines: List[str], top_n: int = 10) -> Dict[str, object]:
    """Perform text analysis on lines.

    Returns a dict containing empty line count, duplicate lines, most frequent words,
    and separation of numeric vs text tokens.
    """
    empty_lines = sum(1 for l in lines if l.strip() == "")
    line_counts = Counter(l.rstrip("\n") for l in lines if l.strip() != "")
    duplicates = {ln: c for ln, c in line_counts.items() if c > 1}

    # Tokenize words (simple) and count frequencies
    tokens = []
    numeric_tokens = []
    text_tokens = []
    for l in lines:
        for t in re.findall(r"[\w\-\.']+", l.lower()):
            tokens.append(t)
            # classify numeric: int or float
            try:
                float(t)
                numeric_tokens.append(t)
            except ValueError:
                text_tokens.append(t)

    word_freq = Counter(t for t in text_tokens if not t.isnumeric())
    most_common = word_freq.most_common(top_n)

    return {
        "empty_lines": empty_lines,
        "duplicate_lines": duplicates,
        "most_frequent_words": most_common,
        "numeric_tokens_sample": numeric_tokens[:50],
        "text_tokens_sample": text_tokens[:50],
    }
