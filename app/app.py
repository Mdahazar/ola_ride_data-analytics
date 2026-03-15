import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("🚖 OLA Ride Insights Dashboard")

# --------------------------
# Load Data
# --------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/ola_cleaned.csv")

df = load_data()

# --------------------------
# Sidebar Filters
# --------------------------

st.sidebar.header("Dashboard Filters")

vehicle_filter = st.sidebar.multiselect(
    "Vehicle Type",
    options=df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)

df = df[
    (df["Vehicle_Type"].isin(vehicle_filter)) &
    (df["Payment_Method"].isin(payment_filter))
]

# --------------------------
# Create Tabs
# --------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings"]
)

# =====================================================
# OVERALL TAB
# =====================================================

with tab1:

    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    total_rides = df.shape[0]
    total_revenue = df["Booking_Value"].sum()
    avg_distance = df["Ride_Distance"].mean()

    col1.metric("Total Rides", f"{total_rides:,}")
    col2.metric("Total Revenue", f"{total_revenue:,.0f}")
    col3.metric("Avg Ride Distance", f"{avg_distance:.2f}")

    rides_over_time = df.groupby("Date").size().reset_index(name="rides")

    fig = px.line(
        rides_over_time,
        x="Date",
        y="rides",
        title="Ride Volume Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# VEHICLE TYPE TAB
# =====================================================

with tab2:

    st.subheader("Vehicle Type Analysis")

    vehicle_counts = df["Vehicle_Type"].value_counts().reset_index()
    vehicle_counts.columns = ["Vehicle Type", "Ride Count"]

    fig = px.bar(
        vehicle_counts,
        x="Vehicle Type",
        y="Ride Count",
        title="Ride Distribution by Vehicle Type",
        color="Vehicle Type"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# REVENUE TAB
# =====================================================

with tab3:

    st.subheader("Revenue Insights")

    revenue = df.groupby("Payment_Method")["Booking_Value"].sum().reset_index()

    fig = px.bar(
        revenue,
        x="Payment_Method",
        y="Booking_Value",
        title="Revenue by Payment Method",
        color="Payment_Method"
    )

    st.plotly_chart(fig, use_container_width=True)

    top_customers = (
        df.groupby("Customer_ID")["Booking_Value"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig2 = px.bar(
        top_customers,
        x="Customer_ID",
        y="Booking_Value",
        title="Top 5 Customers by Revenue",
        color="Customer_ID"
    )

    st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# CANCELLATION TAB
# =====================================================

with tab4:

    st.subheader("Cancellation Analysis")

    status = df["Booking_Status"].value_counts().reset_index()
    status.columns = ["Status", "Count"]

    fig = px.pie(
        status,
        values="Count",
        names="Status",
        title="Ride Cancellation Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# RATINGS TAB
# =====================================================

with tab5:

    st.subheader("Ratings Analysis")

    driver_rating = df["Driver_Ratings"].value_counts().reset_index()
    driver_rating.columns = ["Rating", "Count"]

    fig = px.bar(
        driver_rating,
        x="Rating",
        y="Count",
        title="Driver Ratings Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    customer_rating = df["Customer_Rating"].value_counts().reset_index()
    customer_rating.columns = ["Rating", "Count"]

    fig2 = px.bar(
        customer_rating,
        x="Rating",
        y="Count",
        title="Customer Ratings Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)
