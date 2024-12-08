import streamlit as st
import pandas as pd

# Example data for area chart
data = {
    'Speed': [1, 3, 5, 7, 9],  # X-axis values
    'Velocity': [2, 4, 6, 8, 10]  # Y-axis values
}

df = pd.DataFrame(data)

# Create an area chart
st.subheader("Streamlit Area Chart Example")
st.area_chart(df,x_label='valocity',y_label='speed')

st.write("This is a simple area chart example.")
