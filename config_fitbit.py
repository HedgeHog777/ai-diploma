from pathlib import Path

# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_DIR = Path(
    "/content/drive/MyDrive/FitnessML_Master"
)

RAW_DATA_DIR = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "fitbit"
)

# ============================================================
# GENERAL SETTINGS
# ============================================================

RANDOM_STATE = 42

FIG_DPI = 150