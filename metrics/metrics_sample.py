# Solo-AI - Ratelia Labs
# Copyright © 2025 Gilles C. Obellianne
# License: Apache 2.0

"""
Solo-AI Lite — Metrics Sample
Version minimaliste non-opérationnelle.
"""

import json
from pathlib import Path

OUT_PATH = Path("data/metrics/sample_metrics.json")

def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    metrics = {
        "volatility": 0.0123,
        "mean_return": 0.00042,
        "bullish_candles": 55,
        "bearish_candles": 45
    }
    with open(OUT_PATH, "w") as f:
        json.dump(metrics, f, indent=4)
    print("Sample metrics OK ->", OUT_PATH)

if __name__ == "__main__":
    main()

