import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv(r'./app/compressed-solar-radiation-measurements.csv')

st.title('Solar Radiation Dashboard')

# Display raw data
if st.checkbox('Show Raw Data'):
    st.write(df)

# Summary statistics
if st.checkbox('Show Summary Statistics'):
    st.write(df.describe())

# Plot Global Horizontal Irradiance (GHI) over time
st.subheader('Global Horizontal Irradiance Over Time')
if st.checkbox('Show GHI Plot'):
    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(df['Timestamp']), df['GHI'])
    plt.title('GHI Over Time')
    plt.xlabel('Date')
    plt.ylabel('GHI (W/m²)')
    st.pyplot()

# Temperature Analysis
st.subheader('Temperature Analysis')
if st.checkbox('Show Temperature Plot'):
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Tamb'])
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    st.pyplot()
