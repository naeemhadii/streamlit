import streamlit as st

class LoanApp:
    def __init__(self):
        if "page" not in st.session_state:
            st.session_state.page = "form"
        self.build()

    def build(self):
        if st.session_state.page == "form":
            self.show_form()
        elif st.session_state.page == "results":
            self.show_results()

    def show_form(self):
        st.header("Area Manager")
        st.subheader("Mohsin Shah Sahib")
        
        # Input fields
        st.session_state.loan_amount = st.text_input(
            "Loan Amount", placeholder="Enter loan amount", label_visibility="hidden"
        )
        st.session_state.markup_rate = st.text_input(
            "Markup Rate", placeholder="Enter markup rate", label_visibility="hidden"
        )
        st.session_state.loan_duration = st.text_input(
            "Loan Duration", placeholder="Enter loan duration", label_visibility="hidden"
        )
        st.session_state.processing = st.text_input(
            "Processing", placeholder="Enter processing fees", label_visibility="hidden"
        )
        
        # Button
        if st.button("Calculate", use_container_width=True):
            st.session_state.page = "results"

    def show_results(self):
        st.title("Results Page")
        st.write("Loan Details Submitted:")
        st.write(f"Loan Amount: {st.session_state.loan_amount}")
        st.write(f"Markup Rate: {st.session_state.markup_rate}")
        st.write(f"Loan Duration: {st.session_state.loan_duration}")
        st.write(f"Processing Fees: {st.session_state.processing}")
        if st.button("Go Back"):
            st.session_state.page = "form"


# Instantiate the app
LoanApp()
