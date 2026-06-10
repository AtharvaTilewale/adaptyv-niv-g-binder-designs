"""Plot filtering funnel counts from filtering_funnel_summary.csv."""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    input_csv = base / "processed" / "filtering_funnel_summary.csv"
    output_png = base / "figures" / "filtering_funnel.png"

    df = pd.read_csv(input_csv)

    plt.figure(figsize=(8, 4.5))
    plt.bar(df["stage"], df["output_count"], color="#4C78A8")
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Design count")
    plt.title("NiV-G Binder Design Filtering Funnel")
    plt.tight_layout()
    plt.savefig(output_png, dpi=200)
    plt.close()

    print(f"Filtering funnel plot saved to: {output_png}")


if __name__ == "__main__":
    main()
