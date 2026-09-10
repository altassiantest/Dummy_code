"""CSV file parser and writer utilities."""

import csv
from pathlib import Path


def read_csv(filepath: str) -> list[dict]:
    """Read a CSV file and return list of dicts (uses header row as keys)."""
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(filepath: str, data: list[dict]) -> None:
    """Write list of dicts to CSV file."""
    if not data:
        return
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)


def filter_csv(filepath: str, key: str, value: str) -> list[dict]:
    """Filter CSV rows where key equals value."""
    rows = read_csv(filepath)
    return [row for row in rows if row.get(key) == value]


if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": "30", "city": "NYC"},
        {"name": "Bob", "age": "25", "city": "LA"},
        {"name": "Charlie", "age": "35", "city": "NYC"},
    ]
    tmp = Path("sample.csv")
    write_csv(str(tmp), sample_data)
    print("Read back:", read_csv(str(tmp)))
    print("NYC only:", filter_csv(str(tmp), "city", "NYC"))
    tmp.unlink(missing_ok=True)
