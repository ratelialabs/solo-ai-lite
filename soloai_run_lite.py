"""
Solo-AI Lite — Pipeline Demonstration
"""

import subprocess

steps = [
    "ingest/ingest_sample.py",
    "metrics/metrics_sample.py",
    "patterns/pattern_sample.py",
    "scores/score_engine_sample.py",
    "runtime/risk_daemon_sample.py",
    "insight/insight_sample.py"
]

for step in steps:
    print("\n=== Running:", step, "===")
    subprocess.run(f"python {step}", shell=True, check=True)

print("\nSolo-AI Lite pipeline complete.")

