import streamlit as st
import pandas as pd


class App:
    def __init__(self):
        # Initialize the session state for navigation
        if "page" not in st.session_state:
            st.session_state.page = "index"
        self.build()
        
    def build(self):
        # Check the current page and render accordingly
        if st.session_state.page == "index":
            self.index_page()
        elif st.session_state.page == "result":
            self.result_page()

    def index_page(self):
        self.loan = st.text_input(
            placeholder="Loan Amount", 
            label="loan", 
            label_visibility='collapsed', 
            value=""
        )
        self.markup = st.text_input(
            placeholder="Markup Rate", 
            label="mark", 
            label_visibility="collapsed", 
            value=""
        )
        self.tenor = st.text_input(
            placeholder="Tenor Period", 
            label="tenor", 
            label_visibility="collapsed", 
            value=""
        )
        self.processing = st.text_input(
            placeholder="Processing Rate", 
            label="processing", 
            label_visibility="collapsed", 
            value=""
        )
        
        # Button to navigate to the results page
        if st.button(label="Calculate", use_container_width=True):
            if all([self.loan, self.markup, self.tenor, self.processing]):
                st.session_state.loan = self.loan
                st.session_state.markup = self.markup
                st.session_state.tenor = self.tenor
                st.session_state.processing = self.processing
                st.session_state.page = "result"
            else:
                st.error("Please fill in all the fields!")

    def result_page(self):
        # Results page to display calculations

        st.title("Calculation Results")
        data = {
            "Loan Amount": [st.session_state.loan],
            "Markup Rate": [st.session_state.markup],
            "Tenor Period": [st.session_state.tenor],
            "Processing Rate": [st.session_state.processing],
        }

        df = pd.DataFrame(data)

        # Render the DataTable
        st.write("Loan Information Table")
        st.dataframe(df,use_container_width=True,column_config=None)
        
        if st.button("Go Back"):
            st.session_state.page = "index"


# Instantiate and run the app
App()
