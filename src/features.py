import pandas as pd
import numpy as np


def classify_booking_origin(row):

    if row["agent"] != 0:
        return "Travel Agency"

    elif row["company"] != 0:
        return "Company"

    return "Direct"


def build_features(df: pd.DataFrame) -> pd.DataFrame:

    out = df.copy()

    # -------------------------
    # Total nights
    # -------------------------
    out["total_nights"] = out["stays_in_week_nights"] + out["stays_in_weekend_nights"]

    # -------------------------
    # Total guests
    # -------------------------
    out["total_guests"] = out["adults"] + out["children"] + out["babies"]

    # -------------------------
    # Booking origin
    # -------------------------
    out["booking_origin"] = out.apply(classify_booking_origin, axis=1)

    # -------------------------
    # Room changed
    # -------------------------
    out["room_changed"] = out["reserved_room_type"].astype("string") != out[
        "assigned_room_type"
    ].astype("string")

    # -------------------------
    # Family booking
    # -------------------------
    out["is_family"] = (out["children"] > 0) | (out["babies"] > 0)

    # -------------------------
    # Total stay cost
    # -------------------------
    out["total_stay_cost"] = out["adr"] * out["total_nights"]

    # -------------------------
    # Long stay
    # -------------------------
    out["is_long_stay"] = out["total_nights"] >= 7

    # -------------------------
    # Lead time categories
    # -------------------------
    out["lead_time_category"] = pd.cut(
        out["lead_time"],
        bins=[-1, 7, 30, 90, 365, 1000],
        labels=["Very Short", "Short", "Medium", "Long", "Very Long"],
    )

    # -------------------------
    # ADR categories
    # -------------------------
    out["adr_category"] = pd.qcut(
        out["adr"], q=4, labels=["Low", "Medium", "High", "Luxury"]
    )

    # -------------------------
    # Arrival date
    # -------------------------
    month_map = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    out["arrival_month_num"] = out["arrival_date_month"].map(month_map)

    out["arrival_date"] = pd.to_datetime(
        {
            "year": out["arrival_date_year"],
            "month": out["arrival_month_num"],
            "day": out["arrival_date_day_of_month"],
        }
    )

    # -------------------------
    # Season
    # -------------------------
    out["season"] = np.select(
        [
            out["arrival_month_num"].isin([12, 1, 2]),
            out["arrival_month_num"].isin([3, 4, 5]),
            out["arrival_month_num"].isin([6, 7, 8]),
            out["arrival_month_num"].isin([9, 10, 11]),
        ],
        ["Winter", "Spring", "Summer", "Autumn"],
        default="Unknown",
    )

    return out
