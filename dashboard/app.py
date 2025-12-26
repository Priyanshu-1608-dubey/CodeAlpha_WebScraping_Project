import streamlit as st
import pandas as pd

st.set_page_config(page_title="Web Scraping Dashboard", layout="wide")

st.title("🌐 Web Scraping Data Dashboard")

# Load dataset
df = pd.read_csv("data/quotes.csv")

# Sidebar Filter
st.sidebar.header("Filter Options")
author = st.sidebar.selectbox("Select Author", ["All"] + list(df["Author"].unique()))

if author != "All":
    df = df[df["Author"] == author]

# Display Data
st.subheader("📊 Scraped Quotes Data")
st.dataframe(df)

# Simple Analytics
st.subheader("📈 Quotes Count by Author")
count_df = df["Author"].value_counts()
st.bar_chart(count_df)
