# utils/data_loader.py
import json
import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv_rows(filename):
    with open(DATA_DIR / filename, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
