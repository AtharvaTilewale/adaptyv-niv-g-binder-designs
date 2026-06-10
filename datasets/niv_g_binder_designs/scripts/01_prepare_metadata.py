"""Prepare processed metadata tables from template design metrics."""

from pathlib import Path
import pandas as pd


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    input_csv = base / "processed" / "all_design_metrics_template.csv"
    output_csv = base / "processed" / "all_design_metrics_prepared.csv"

    df = pd.read_csv(input_csv)
    if "sequence_length" not in df.columns and "sequence" in df.columns:
        df["sequence_length"] = df["sequence"].str.len()

    df.to_csv(output_csv, index=False)
    print(f"Prepared metadata: {output_csv}")


if __name__ == "__main__":
    main()
