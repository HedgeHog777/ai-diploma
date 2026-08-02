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

FIG_DPI = 200

SAVE_TABLES = True
SAVE_FIGURES = True

# ============================================================
# LOCALIZATION
# ============================================================

COLUMN_LABELS = {

    "user_id": "Ідентифікатор користувача",
    "date": "Дата",

    "gender": "Стать",
    "age": "Вік",

    "height_cm": "Зріст, см",
    "weight_kg": "Вага, кг",
    "bmi": "Індекс маси тіла",

    "heart_rate": "Частота серцевих скорочень",
    "blood_pressure": "Артеріальний тиск",

    "steps": "Кількість кроків",
    "distance_km": "Пройдена відстань, км",

    "calories_burned": "Спалені калорії",
    "exercise_minutes": "Фізична активність, хв",

    "sleep_hours": "Тривалість сну, год",

    "stress_level": "Рівень стресу",

    "water_intake_liters": "Споживання води, л",

    "daily_calories": "Добова калорійність",

    "activity_level": "Рівень активності",

    "mood": "Настрій"
}

VALUE_LABELS = {

    "Male": "Чоловік",
    "Female": "Жінка"

}
# ============================================================
# CREATE DIRECTORIES
# ============================================================

for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    FIGURES_DIR,
    TABLES_DIR,
    REPORTS_DIR,
    MODELS_DIR,
    THESIS_DIR,
    NOTEBOOKS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)