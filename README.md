# python-file-analyzer

Small, beginner-friendly Python project to analyze `.txt`, `.csv`, and `.log` files.

Features
- Safe file reading with error handling
- File metadata (size, lines, words, characters)
- Text analysis (empty lines, duplicate lines, most frequent words, numeric vs text)
- CSV analysis (rows/columns, missing values, dtypes, basic statistics) using `pandas`
- Log analysis (error/warning counts, keyword search, IP detection, timeline by hour)

Quick start

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the analyzer:

```bash
python file_analyzer.py sample.log
python file_analyzer.py data.csv
```

Project layout

- `file_analyzer/` - package modules (core, csv_analyzer, log_analyzer, utils)
- `file_analyzer.py` - CLI entry
- `requirements.txt` - dependencies

This project is intentionally small and modular so students and researchers can extend
parsers, add richer log parsing, or integrate visualization later.
