import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean hotel booking dataset.
    """

    out = df.copy()

    # -------------------------
    # Column names snake_case
    # -------------------------
    out.columns = (
        out.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
    )

    # -------------------------
    # Remove sensitive columns
    # -------------------------
    sensitive_cols = ["name", "email", "phone_number", "credit_card"]

    existing_sensitive = [col for col in sensitive_cols if col in out.columns]

    out = out.drop(columns=existing_sensitive)

    # -------------------------
    # Missing values
    # -------------------------

    # children -> only 4 nulls
    out["children"] = out["children"].fillna(0)

    # agent/company null means no agency/company
    out["agent"] = out["agent"].fillna(0)
    out["company"] = out["company"].fillna(0)

    # -------------------------
    # Data types
    # -------------------------
    categorical_cols = [
        "hotel",
        "meal",
        "market_segment",
        "distribution_channel",
        "deposit_type",
        "customer_type",
        "reserved_room_type",
        "assigned_room_type",
        "arrival_date_month",
    ]

    for col in categorical_cols:
        out[col] = out[col].astype("category")

    # -------------------------
    # Remove duplicates
    # -------------------------
    # out = out.drop_duplicates()

    return out
