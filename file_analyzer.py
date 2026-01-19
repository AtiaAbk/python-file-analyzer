#python file analyzer 

import argparse
import os
import sys

from file_analyzer import (
    read_file,
    get_metadata,
    analyze_text,
    analyze_csv,
    analyze_log,
    print_summary,
)


def detect_type(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".csv":
        return "csv"
    if ext in {".log"}:
        return "log"
    return "text"


def main():
    parser = argparse.ArgumentParser(description="Analyze a file (text, CSV, log)")
    parser.add_argument("path", help="Path to file to analyze")
    args = parser.parse_args()
    p = args.path

    if not os.path.exists(p):
        print(f"File not found: {p}")
        sys.exit(2)

    ftype = detect_type(p)

    try:
        if ftype == "csv":
            try:
                summary = analyze_csv(p)
            except Exception as e:
                print("Failed to parse CSV with pandas:", e)
                sys.exit(3)
        else:
            lines = read_file(p)
            metadata = get_metadata(p, lines)
            text_summary = analyze_text(lines)
            if ftype == "log":
                log_summary = analyze_log(lines)
                summary = {"metadata": metadata, "text": text_summary, "log": log_summary}
            else:
                summary = {"metadata": metadata, "text": text_summary}

        print_summary(summary)
    except PermissionError:
        print(f"Permission denied reading file: {p}")
        sys.exit(4)
    except Exception as e:
        print("Unexpected error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
