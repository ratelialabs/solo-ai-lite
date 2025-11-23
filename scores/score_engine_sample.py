"""
Solo-AI Lite — Score Engine Mock
Combinaison minimaliste de métriques et patterns.
"""

import json
from pathlib import Path

METRICS = Path("data/metrics/sample_metrics.json")
PATTERNS = Path("data/patterns/sample_patterns.json")
OUT_PATH = Path("data/scores/sample_scores.json")

def main():
    with open(METRICS, "r") as f:
        m = json.load(f)
    with open(PATTERNS, "r") as f:
        p = json.load(f)

    sentiment = 0.1  # Valeur fixe pour la version Lite

    results = {
        "pattern_scores": p,
        "market_scores": m,
        "sentiment": sentiment
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=4)

    print("Sample score engine OK ->", OUT_PATH)

if __name__ == "__main__":
    main()

