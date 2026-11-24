import streamlit as st
from forecasting.prediction import forecast_consumption
from analysis.consumption import analyse_consumption
from analysis.visualisation import (
    plot_daily_consumption,
    plot_monthly_consumption
)


# Page configuration
st.set_page_config(
    page_title="WattWise",
    page_icon="",
    layout="wide"
)


# Dashboard heading
st.title(" WattWise")

st.write(
    "Electricity Consumption Analysis and Forecasting System"
)

st.markdown("---")


# Load dashboard data
@st.cache_data
def get_dashboard_data():
    return analyse_consumption()


daily, monthly, df = get_dashboard_data()


# Summary section
st.subheader("Consumption Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Daily Consumption",
    f"{daily.mean():.2f} kWh"
)

col2.metric(
    "Highest Daily Consumption",
    f"{daily.max():.2f} kWh"
)

col3.metric(
    "Lowest Daily Consumption",
    f"{daily.min():.2f} kWh"
)


st.markdown("---")


# Daily consumption graph
st.subheader("Daily Electricity Consumption")

daily_fig = plot_daily_consumption(daily)

st.pyplot(daily_fig)


# Monthly consumption graph
st.subheader("Monthly Electricity Consumption")

monthly_fig = plot_monthly_consumption(monthly)

st.pyplot(monthly_fig)

st.markdown("---")

# Electricity consumption forecast
st.subheader(" 7-Day Electricity Consumption Forecast")

forecast = forecast_consumption(daily)

st.write(
    "Estimated electricity consumption for the next seven days "
    "based on historical consumption trends."
)

st.dataframe(
    forecast.round(2),
    use_container_width=True
)


# Dataset preview
st.subheader("Dataset Preview")

st.write("Here are the first 10 records from the cleaned dataset.")

st.dataframe(
    df.head(10),
    use_container_width=True
)


st.success("WattWise is running successfully!")