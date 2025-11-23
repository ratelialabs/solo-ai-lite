"""
Solo-AI Lite — Insight Report (Demo)
"""

from pathlib import Path

OUT = Path("data/insights/sample_report.md")

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("# Solo-AI Lite — Insight Report\n\nRapport démonstratif.")
    print("Sample insight OK ->", OUT)

if __name__ == "__main__":
    main()

