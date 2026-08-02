"""
============================================================
Utility functions
============================================================
"""

import pandas as pd
import config


# ============================================================
# DATASET
# ============================================================

def load_dataset():
    """Load original dataset."""
    return pd.read_csv(config.DATASET_PATH)


# ============================================================
# TABLES
# ============================================================

def save_table(df, filename, index=True):
    """Save DataFrame as CSV."""

    path = config.TABLES_DIR / filename

    df.to_csv(path, index=index)

    print(f"✓ Table saved -> {path}")


# ============================================================
# FIGURES
# ============================================================

def save_figure(fig, filename):
    """Save matplotlib figure."""

    path = config.FIGURES_DIR / filename

    fig.savefig(
        path,
        dpi=config.FIG_DPI,
        bbox_inches="tight"
    )

    print(f"✓ Figure saved -> {path}")


# ============================================================
# REPORTS
# ============================================================

def save_report(text, filename):
    """Save text or markdown report."""

    path = config.REPORTS_DIR / filename

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✓ Report saved -> {path}")
    
    # ============================================================
# LOCALIZATION
# ============================================================

def label(column):
    """
    Return localized column name.
    """
    return config.COLUMN_LABELS.get(column, column)


def rename_columns(df):
    """
    Return dataframe with localized column names.
    """
    return df.rename(columns=config.COLUMN_LABELS)


def localize_values(series):
    """
    Replace categorical values using VALUE_LABELS.
    """
    return series.replace(config.VALUE_LABELS)
    
    
    def xlabel(ax, column):
    ax.set_xlabel(label(column))


def ylabel(ax, column):
    ax.set_ylabel(label(column))


def title(ax, text):
    ax.set_title(text)
    
    def save_table_ua(df, filename, index=True):
    """
    Save table with localized column names.
    """

    localized = rename_columns(df)

    save_table(localized, filename, index=index)