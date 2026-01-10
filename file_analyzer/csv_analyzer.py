"""CSV-specific analysis using pandas."""
from typing import Dict, Any
import pandas as pd


def analyze_csv(path: str) -> Dict[str, Any]:
    """Analyze a CSV file and return summary info.

    Uses pandas for robust parsing. Caller should handle exceptions.
    """
    df = pd.read_csv(path)
    rows, cols = df.shape
    missing_per_column = df.isnull().sum().to_dict()
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}
    # Basic statistical summary for numeric columns
    stats = df.describe(include='all').to_dict()

    return {
        "rows": rows,
        "columns": cols,
        "missing_per_column": missing_per_column,
        "dtypes": dtypes,
        "stats_sample": stats,
    }
