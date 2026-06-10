"""Plot ipSAE scores by design from all_design_metrics_template.csv."""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    input_csv = base / "processed" / "all_design_metrics_template.csv"
    output_png = base / "figures" / "ipsae_scores.png"

    df = pd.read_csv(input_csv).sort_values("ipSAE", ascending=False)

    plt.figure(figsize=(7.5, 4.5))
    plt.bar(df["design_id"], df["ipSAE"], color="#59A14F")
    plt.ylabel("ipSAE")
    plt.xlabel("design_id")
    plt.title("ipSAE Scores by Design")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(output_png, dpi=200)
    plt.close()

    print(f"ipSAE score plot saved to: {output_png}")


if __name__ == "__main__":
    main()
