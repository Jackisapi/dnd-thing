import streamlit as st
import pandas as pd

st.title('Weekly Data Visualization')

# Load data
data = st.file_uploader("Please upload your csv file", type=['csv'])
while data is None:
    continue

data = pd.read_csv(data)

# Set page title
st.title('Weekly Data Visualization')

# Display the dataframe
st.write(data)

# Plot the data
st.line_chart(data.set_index('name').T)
