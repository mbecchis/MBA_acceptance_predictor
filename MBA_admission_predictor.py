import streamlit as st
from model_intro import introduction_page
from model_prediction import predictor_page

def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio(
        "Choose a page:",
        ["Introduction", "Acceptance Predictor"]  # Ensure options match the checks below
    )
    
    if selection == "Introduction":
        introduction_page()
    elif selection == "Acceptance Predictor":
        predictor_page()  # Fixed the capitalization to match the radio option

if __name__ == "__main__":
    main()
