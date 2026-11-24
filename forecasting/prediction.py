import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression


def forecast_consumption(daily_consumption):

    # Prepare historical data
    data = daily_consumption.dropna()

    # Convert dates into numerical values
    X = np.arange(len(data)).reshape(-1, 1)

    # Electricity consumption values
    y = data.values

    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the next 7 days
    future_days = np.arange(
        len(data),
        len(data) + 7
    ).reshape(-1, 1)

    predictions = model.predict(future_days)

    # Generate future dates
    future_dates = pd.date_range(
        start=data.index[-1] + pd.Timedelta(days=1),
        periods=7,
        freq="D"
    )

    # Store predictions in a DataFrame
    forecast = pd.DataFrame({
        "Date": future_dates,
        "Predicted Consumption (kWh)": predictions
    })

    return forecast