# from pathlib import Path
# import sys

# try:
#     ROOT = Path(__file__).resolve().parent.parent
# except NameError:
#     # __file__ no existe en notebooks, usar cwd
#     ROOT = Path.cwd().parent

# RAW_PATH = ROOT / "data" / "raw" / "hotel_booking.csv"
# OUT_PATH = ROOT / "data" / "processed" / "clean_dataset.csv"

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Change these paths to point to your data files
RAW_PATH = ROOT / "data" / "raw" / "raw_dataset.csv"
OUT_PATH = ROOT / "data" / "processed" / "clean_dataset.csv"
