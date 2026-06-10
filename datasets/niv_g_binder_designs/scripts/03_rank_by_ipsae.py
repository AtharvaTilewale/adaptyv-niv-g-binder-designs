"""Rank designs by ipSAE and export a ranked table."""

from pathlib import Path
import pandas as pd


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    input_csv = base / "processed" / "all_design_metrics_template.csv"
    output_csv = base / "processed" / "all_design_ipsae_ranked.csv"

    df = pd.read_csv(input_csv)
    ranked = df.sort_values("ipSAE", ascending=False).reset_index(drop=True)
    ranked.insert(0, "rank", ranked.index + 1)

    ranked.to_csv(output_csv, index=False)
    print(f"ipSAE ranking written to: {output_csv}")


if __name__ == "__main__":
    main()
