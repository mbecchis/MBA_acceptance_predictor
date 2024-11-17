import streamlit as st

def introduction_page():
    # Add custom CSS for font styling
    st.markdown(
        """
        <style>
        h1 {
            font-family: 'Verdana', sans-serif;
            font-size: 48px;
            color: #2e8b57; /* Green for the main title */
            text-align: center; /* Center the main title */
        }
        h2 {
            font-family: 'Arial', sans-serif;
            color: #4682b4; /* Steel blue for subtitles */
        }
        .dataset-info {
            font-size: 18px; /* Font size for dataset information */
            color: #555555; /* Dark grey for contrast */
        }
        p, li {
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Page content
    st.title("🎓 MBA Admission Predictor - Wharton University")
    st.image("wharton_image", use_column_width=True)  # Ensure the correct file name for the image

    st.subheader("🌟 Introduction")
    st.markdown("""
    Welcome to the **MBA Admission Predictor**! This project leverages Artificial Neural Networks to help aspiring MBA candidates predict their admission outcomes to the prestigious Wharton University. 🎯
    
    Use our predictor to input your details and receive an instant prediction of your admission status! 📊
    """)

    st.subheader("📂 About the Dataset")
    st.image("dataset.jpg", use_column_width=True)  # Ensure the correct file name for the image

    st.markdown("""
    The dataset used in this project contains synthetic data based on the statistics of Wharton University's Class of 2025. This data serves as the foundation for training the predictive model. 🤖
    
    ### **Key Features:**
    - **`application_id`**: Unique identifier for each application
    - **`gender`**: Applicant's gender (Male, Female) 🚻
    - **`international`**: International student status (TRUE/FALSE) 🌍
    - **`gpa`**: Grade Point Average (on a 4.0 scale) 📘
    - **`major`**: Undergraduate major (e.g., Business, STEM, Humanities) 📚
    - **`race`**: Applicant's racial background (e.g., White, Black, Asian, Hispanic, Other) 🌎
    - **`gmat`**: GMAT score (max: 800 points) 📊
    - **`work_exp`**: Number of years of work experience 💼
    - **`work_industry`**: Industry of previous work experience (e.g., Consulting, Finance, Technology) 🏢
    - **`admission`**: Admission status (Admit, Waitlist, Null: Deny) ✅/❌
    """)

    st.write("💾 [Link to the Dataset](https://www.kaggle.com/datasets/taweilo/mba-admission-dataset)")

    st.markdown("""
    ---
    ✍️ **Note**: For more information on how the model was trained, refer to the detailed comments in the code.
    """)

# Display the introduction page
introduction_page()
