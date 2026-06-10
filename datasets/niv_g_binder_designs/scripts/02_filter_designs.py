"""Apply simple RMSD and confidence filters to design metrics."""

from pathlib import Path
import pandas as pd


PLDDT_MIN = 75.0
PTM_MIN = 0.60
IPTM_MIN = 0.60
RMSD_MAX = 2.50


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    input_csv = base / "processed" / "all_design_metrics_template.csv"
    output_csv = base / "processed" / "all_design_metrics_filtered.csv"

    df = pd.read_csv(input_csv)
    passed = (
        (df["pLDDT"] >= PLDDT_MIN)
        & (df["pTM"] >= PTM_MIN)
        & (df["ipTM"] >= IPTM_MIN)
        & (df["RMSD"] <= RMSD_MAX)
    )
    df["passed_filter"] = passed

    df.to_csv(output_csv, index=False)
    print(f"Filtered designs written to: {output_csv}")


if __name__ == "__main__":
    main()
