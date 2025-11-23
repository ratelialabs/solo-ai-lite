"""
Solo-AI Lite — Pattern Detector (Mock)
Ce fichier montre comment Solo-AI structure les patterns.
"""

import json
from pathlib import Path

OUT_PATH = Path("data/patterns/sample_patterns.json")

def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    patterns = {
        "FVG_total": 12,
        "MA_cross_total": 3,
        "RSI_signals": 5
    }
    with open(OUT_PATH, "w") as f:
        json.dump(patterns, f, indent=4)
    print("Sample patterns OK ->", OUT_PATH)

if __name__ == "__main__":
    main()

