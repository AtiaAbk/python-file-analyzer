"""file_analyzer package entrypoints."""
from .core import read_file, get_metadata, analyze_text
from .csv_analyzer import analyze_csv
from .log_analyzer import analyze_log
from .utils import print_summary

__all__ = [
    "read_file",
    "get_metadata",
    "analyze_text",
    "analyze_csv",
    "analyze_log",
    "print_summary",
]
