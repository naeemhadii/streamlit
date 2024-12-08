import streamlit as st
import pandas as pd

# Example data for area chart
data = {
    'Speed': [1, 3, 5, 7, 9],  # X-axis values
    'Velocity': [2, 4, 6, 8, 10]  # Y-axis values
}

df = pd.DataFrame(data)

# Function to handle chat input submission
def called(value):
    st.write(f"User Input recieved: {value}")

# Create an area chart
st.subheader("Streamlit Area Chart Example")
st.area_chart(df)

# Chat input with a callback
user_input = st.chat_input(placeholder="Type something here...", key="chatbox")
if user_input:  # When user submits input
    called(user_input)

st.write("This is a simple area chart example.")
