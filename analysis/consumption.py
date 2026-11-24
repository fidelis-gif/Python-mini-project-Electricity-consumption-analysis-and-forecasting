from analysis.preprocessing import load_data, clean_data


def analyse_consumption():

    print("Loading and processing electricity data...")

    df = load_data()
    df = clean_data(df)

    # Set Timestamp as index
    df = df.set_index("Timestamp")

    # Calculate daily energy consumption
    daily_consumption = (
        df["Energy_A_plus"].resample("D").sum()
    )

    # Calculate monthly energy consumption
    monthly_consumption = (
        df["Energy_A_plus"].resample("ME").sum()
    )

    print("\n========== ELECTRICITY CONSUMPTION ANALYSIS ==========")

    print("\nTotal Records:", len(df))

    print("\nAverage Daily Consumption (kWh):")
    print(round(daily_consumption.mean(), 2))

    print("\nHighest Daily Consumption (kWh):")
    print(round(daily_consumption.max(), 2))

    print("\nLowest Daily Consumption (kWh):")
    print(round(daily_consumption.min(), 2))

    print("\nMonthly Consumption (kWh):")
    print(monthly_consumption.round(2))

    return daily_consumption, monthly_consumption, df


if __name__ == "__main__":
    analyse_consumption()