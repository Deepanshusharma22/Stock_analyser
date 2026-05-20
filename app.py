according to this code
import streamlit as st
import pandas as pd
from datetime import datetime

# Page settings
st.set_page_config(
    page_title="Bull Run Stocks",
    page_icon="📈",
    layout="centered"
)

# Title
st.title("Find stocks for profit ")

st.write("Click button to load latest BUY stocks")

# Refresh button
if st.button("🔄 Refresh Stocks"):

    # Google Sheet details
    sheet_id = "1fnCuLtx5ywhKImdYlShMtVlH3BV_-6TvdvRauZvVZu0"
    sheet_name = "Final_List"

    # Google Sheet URL
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    # Read data
    df = pd.read_csv(url)

    # Keep useful columns only
    df = df[[
        "Stocks In Bull Run NSE Code",
        "CMP",
        "Cumulative Average Rule (CAR) Rating"
    ]]

    # Filter BUY stocks
    buy_stocks = df[
        df["Cumulative Average Rule (CAR) Rating"] == "Buy/Average Out"
    ]

    # Keep only needed columns
    buy_stocks = buy_stocks[[
        "Stocks In Bull Run NSE Code",
        "CMP"
    ]]

    # Rename columns
    buy_stocks.columns = ["Stock", "CMP"]

    # Success message
    st.success("Latest stocks loaded successfully ✅")

    # Show total stocks
    st.metric("Total BUY Stocks", len(buy_stocks))

    # Show dataframe
    st.dataframe(
        buy_stocks,
        hide_index=True,
        width="stretch"
    )
