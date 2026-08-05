"""
============================================================
FitnessML Master Thesis
Utility Functions
============================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import config


# ============================================================
# DATASET
# ============================================================

def load_dataset():
    """
    Load the original dataset.
    """

    return pd.read_csv(config.DATASET_PATH)


# ============================================================
# SAVE FILES
# ============================================================

def save_table(df, filename, index=True):
    """
    Save DataFrame as CSV.
    """

    if not config.SAVE_TABLES:
        return

    path = config.TABLES_DIR / filename

    df.to_csv(
        path,
        index=index,
        encoding=config.REPORT_ENCODING
    )

    print(f"✓ Table saved -> {path}")


def save_table_ua(df, filename, index=True):
    """
    Save DataFrame with localized column names.
    """

    localized = rename_columns(df)

    save_table(
        localized,
        filename,
        index=index
    )


def save_report(text, filename):
    """
    Save Markdown/Text report.
    """

    if not config.SAVE_REPORTS:
        return

    path = config.REPORTS_DIR / filename

    with open(
        path,
        "w",
        encoding=config.REPORT_ENCODING
    ) as f:

        f.write(text)

    print(f"✓ Report saved -> {path}")


def save_figure(fig, filename):
    """
    Save matplotlib figure.
    """

    if not config.SAVE_FIGURES:
        return

    path = config.FIGURES_DIR / filename

    fig.savefig(
        path,
        dpi=config.FIG_DPI,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"✓ Figure saved -> {path}")


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
    Rename DataFrame columns using localization dictionary.
    """

    return df.rename(columns=config.COLUMN_LABELS)


def localize_values(series):
    """
    Replace categorical values with localized versions.
    """

    return series.replace(config.VALUE_LABELS)


# ============================================================
# MATPLOTLIB HELPERS
# ============================================================

def xlabel(ax, column):

    ax.set_xlabel(label(column))


def ylabel(ax, column):

    ax.set_ylabel(label(column))


def title(ax, text):

    ax.set_title(text)


# ============================================================
# VISUALIZATION
# ============================================================

def set_plot_style():
    """
    Apply global plotting style.
    """

    sns.set_theme(
        style=config.STYLE,
        palette=config.PALETTE
    )


# ============================================================
# CONSOLE OUTPUT
# ============================================================

def section(text):
    """
    Print formatted section header.
    """

    print("\n" + "=" * 60)
    print(text.upper())
    print("=" * 60)


def subsection(text):
    """
    Print formatted subsection header.
    """

    print("\n" + "-" * 40)
    print(text)
    print("-" * 40)