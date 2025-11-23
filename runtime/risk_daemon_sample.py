"""
Solo-AI Lite — Risk Daemon (Simulation)
"""

import json
from pathlib import Path
from datetime import datetime

DECISION = Path("data/scores/sample_scores.json")
LOG = Path("logs/risk_daemon_lite.log")

def main():
    with open(DECISION, "r") as f:
        data = json.load(f)

    sentiment = data.get("sentiment", 0.0)

    if sentiment > 0.2:
        action = "BUY"
    elif sentiment < -0.2:
        action = "SELL"
    else:
        action = "HOLD"

    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a") as f:
        f.write(f"{datetime.utcnow()} | sentiment={sentiment} | action={action}\n")

    print("Risk Daemon Lite OK -> action:", action)

if __name__ == "__main__":
    main()

