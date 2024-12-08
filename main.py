import streamlit as st

class App:
    def __init__(self):
        self.show_form()
    def show_form(self):
        st.header("Area Manager")
        st.subheader("Mohsin Shah Sahib")
        st.divider()

        # Create a container to group inputs
        with st.container():
            col1, col2 = st.columns(2)  # Two columns for a more compact layout
            
            with col1:
                st.session_state.loan_amount = st.text_input("Loan Amount",placeholder="Enter loan amount",label_visibility="hidden",value=st.session_state.get("loan_amount", ""))
                st.session_state.loan_duration = st.text_input("Loan Duration",placeholder="Enter loan duration",label_visibility="hidden",value=st.session_state.get("loan_duration", ""))
            
            with col2:
                st.session_state.markup_rate = st.text_input(
                    "Markup Rate",
                    placeholder="Enter markup rate",
                    label_visibility="hidden",
                    value=st.session_state.get("markup_rate", "")
                )
                st.session_state.processing = st.text_input(
                    "Processing",
                    placeholder="Enter processing fees",
                    label_visibility="hidden",
                    value=st.session_state.get("processing", "")
                )

        # Button for navigation
        if st.button("Calculate", use_container_width=True):
            if all([st.session_state.loan_amount, st.session_state.markup_rate, st.session_state.loan_duration, st.session_state.processing]):
                st.session_state.page = "results"
            else:
                st.error("Please fill in all the fields before calculating.")
App()
