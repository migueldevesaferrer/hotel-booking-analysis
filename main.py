from pathlib import Path

from src.io import load_csv
from src.cleaning import clean
from src.features import build_features


def main():
    # root = Path(__file__).resolve().parent
    # raw_path = root / "data" / "raw" / "hotel_booking.csv"
    # out_path = root / "data" / "processed" / "hotel_booking_clean_features.csv"

    file_path = "data/raw/hotel_booking.csv"

    df = load_csv(raw_path)
    df = clean(df)
    df = build_features(df)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
