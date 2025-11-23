"""
Solo-AI Lite — Sample Ingest
Ce fichier simule l’ingestion de données marché.

La version complète Solo-AI utilise des flux marché réels (Binance),
mais ce module est volontairement simplifié pour la démonstration publique.
"""

import json
from pathlib import Path

OUT_PATH = Path("data/raw/sample_ohlcv.json")

def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    sample_data = {
        "symbol": "BTCUSDT",
        "timeframe": "1h",
        "data": [
            [1700000000, 35000, 35100, 34900, 35050, 123.45],  # timestamp, OHLCV
            [1700003600, 35050, 35200, 35000, 35120, 150.12],
        ]
    }
    with open(OUT_PATH, "w") as f:
        json.dump(sample_data, f, indent=4)
    print("Sample ingest OK ->", OUT_PATH)

if __name__ == "__main__":
    main()

