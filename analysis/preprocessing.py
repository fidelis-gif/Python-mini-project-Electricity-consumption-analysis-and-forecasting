import pandas as pd
from pathlib import Path

DATA_FOLDER = Path(__file__).resolve().parent.parent / "data"


def load_data():

    print("Loading electricity datasets...")

    df_2024 = pd.read_csv(DATA_FOLDER / "2024_UTC.csv")
    df_2025 = pd.read_csv(DATA_FOLDER / "2025_UTC.csv")

    # Combine both datasets
    df = pd.concat([df_2024, df_2025], ignore_index=True)

    return df


def clean_data(df):

    print("Cleaning electricity data...")

    # Convert timestamps to datetime
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"],
        utc=True,
        errors="coerce"
    )

    # Convert energy values to numeric
    df["Energy_A_plus"] = pd.to_numeric(
        df["Energy_A_plus"],
        errors="coerce"
    )

    # Remove missing and invalid records
    df.dropna(inplace=True)

    # Sort records by timestamp
    df = df.sort_values("Timestamp")

    # Remove duplicate timestamps
    df = df.drop_duplicates(subset=["Timestamp"])

    df.reset_index(drop=True, inplace=True)

    print("Dataset cleaned successfully!")

    return df