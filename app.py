import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Bull Run Stocks",
    page_icon="📈",
    layout="centered"
)

# ---------------- AUTO REFRESH ----------------
# Auto refresh every 30 seconds
st_autorefresh(interval=30000, key="refresh")

# ---------------- TITLE ----------------
st.title("📈 Find Stocks For Profit")

st.write("Click button to load latest BUY stocks")

# ---------------- GOOGLE SHEET DETAILS ----------------
sheet_id = "1fnCuLtx5ywhKImdYlShMtVlH3BV_-6TvdvRauZvVZu0"
sheet_name = "Final_List"

# Google Sheet CSV URL
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# ---------------- LOAD DATA FUNCTION ----------------
@st.cache_data(ttl=30)
def load_data():
    df = pd.read_csv(url)

    # Keep useful columns
    df = df[[
        "Stocks In Bull Run NSE Code",
        "CMP",
        "Cumulative Average Rule (CAR) Rating"
    ]]

    # Filter BUY stocks
    buy_stocks = df[
        df["Cumulative Average Rule (CAR) Rating"] == "Buy/Average Out"
    ]

    # Keep only required columns
    buy_stocks = buy_stocks[[
        "Stocks In Bull Run NSE Code",
        "CMP"
    ]]

    # Rename columns
    buy_stocks.columns = ["Stock", "CMP"]

    return buy_stocks

# ---------------- BUTTON ----------------
if st.button("🔄 Refresh Stocks"):

    # Load latest data
    buy_stocks = load_data()

    # Success message
    st.success("Latest stocks loaded successfully ✅")

    # Current refresh time
    current_time = datetime.now().strftime("%H:%M:%S")

    # Show refresh time
    st.info(f"🕒 Last Updated: {current_time}")

    # Total stocks
    st.metric("Total BUY Stocks", len(buy_stocks))

    # Show dataframe
    st.dataframe(
        buy_stocks,
        hide_index=True,
        use_container_width=True
    )
