"""
============================================================
FitnessML Master Thesis
Project Configuration
============================================================
"""

from pathlib import Path

# ============================================================
# PROJECT
# ============================================================

PROJECT_DIR = Path("/content/drive/MyDrive/FitnessML_Master")

# ============================================================
# DIRECTORIES
# ============================================================

DATA_DIR = PROJECT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

FIGURES_DIR = PROJECT_DIR / "figures"
TABLES_DIR = PROJECT_DIR / "tables"
REPORTS_DIR = PROJECT_DIR / "reports"
MODELS_DIR = PROJECT_DIR / "models"
THESIS_DIR = PROJECT_DIR / "thesis"
NOTEBOOKS_DIR = PROJECT_DIR / "notebooks"

# ============================================================
# DATASET
# ============================================================

DATASET_NAME = "health_fitness_tracking_365days.csv"
DATASET_PATH = RAW_DATA_DIR / DATASET_NAME

# ============================================================
# EXPERIMENT SETTINGS
# ============================================================

RANDOM_STATE = 42

TEST_SIZE = 0.20
VALIDATION_SIZE = 0.20

# ============================================================
# VISUALIZATION
# ============================================================

FIG_DPI = 200
FIGSIZE = (10, 6)

STYLE = "whitegrid"
PALETTE = "viridis"

LANGUAGE = "uk"

# ============================================================
# EXPORT
# ============================================================

SAVE_TABLES = True
SAVE_FIGURES = True
SAVE_REPORTS = True

REPORT_ENCODING = "utf-8"

# ============================================================
# LOCALIZATION
# ============================================================

COLUMN_LABELS = {

    "user_id": "Ідентифікатор користувача",
    "date": "Дата",

    "gender": "Стать",
    "age": "Вік",

    "steps": "Кількість кроків",
    "heart_rate_avg": "Середній пульс",
    "sleep_hours": "Тривалість сну (год)",
    "calories_burned": "Спалені калорії",
    "exercise_minutes": "Фізична активність (хв)",
    "stress_level": "Рівень стресу",
    "weight_kg": "Вага (кг)",
    "bmi": "Індекс маси тіла"
}

VALUE_LABELS = {

    "M": "Чоловік",
    "F": "Жінка"

}

# ============================================================
# CREATE PROJECT DIRECTORIES
# ============================================================

DIRECTORIES = [

    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,

    FIGURES_DIR,
    TABLES_DIR,
    REPORTS_DIR,

    MODELS_DIR,
    THESIS_DIR,
    NOTEBOOKS_DIR

]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)