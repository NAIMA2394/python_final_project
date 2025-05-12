import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv("owid-covid-data.csv")
df['date'] = pd.to_datetime(df['date'])

# App title
st.title("🌍 COVID-19 Global Data Tracker")

# User input
country = st.selectbox("Select a Country", sorted(df['location'].dropna().unique()))
start_date = st.date_input("Start Date", value=pd.to_datetime("2021-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2021-12-31"))

# Filter data
filtered_df = df[(df['location'] == country) &
                 (df['date'] >= pd.to_datetime(start_date)) &
                 (df['date'] <= pd.to_datetime(end_date))]

# Show basic stats
st.subheader(f"📊 Data for {country}")
st.write(filtered_df[['date', 'total_cases', 'total_deaths', 'new_cases', 'new_deaths']].head())

# Line chart
st.subheader("📈 Total Cases Over Time")
st.line_chart(filtered_df.set_index('date')['total_cases'])

st.subheader("💀 Total Deaths Over Time")
st.line_chart(filtered_df.set_index('date')['total_deaths'])
