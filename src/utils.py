from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def assert_columns(df, required):

    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")


def save_plot(fig, filename: str):

    output_dir = Path("reports/figures")

    output_dir.mkdir(parents=True, exist_ok=True)

    fig.savefig(output_dir / filename, bbox_inches="tight")

    print(f"Saved plot: {filename}")


def set_plot_style():

    plt.style.use("ggplot")


def missing_values_table(df):

    missing = df.isnull().sum()

    percent = (df.isnull().sum() / len(df)) * 100

    return pd.DataFrame({"missing_values": missing, "percentage": percent}).sort_values(
        by="percentage", ascending=False
    )


def numerical_summary(df):

    return df.describe().T.sort_values(by="mean", ascending=False)
