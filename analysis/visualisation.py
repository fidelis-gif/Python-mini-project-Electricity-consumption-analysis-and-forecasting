import matplotlib.pyplot as plt


def plot_daily_consumption(daily_consumption):

    fig, ax = plt.subplots(figsize=(12, 5))

    recent_data = daily_consumption.tail(30)

    ax.plot(
        recent_data.index,
        recent_data.values,
        marker="o"
    )

    ax.set_title("Daily Electricity Consumption")
    ax.set_xlabel("Date")
    ax.set_ylabel("Energy Consumption (kWh)")

    ax.tick_params(axis="x", rotation=45)
    ax.grid(True)

    fig.tight_layout()

    return fig


def plot_monthly_consumption(monthly_consumption):

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(
        monthly_consumption.index.strftime("%b %Y"),
        monthly_consumption.values
    )

    ax.set_title("Monthly Electricity Consumption")
    ax.set_xlabel("Month")
    ax.set_ylabel("Energy Consumption (kWh)")

    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y")

    fig.tight_layout()

    return fig