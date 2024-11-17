import streamlit as st

def introduction_page():
    # Add custom CSS for background color, title font, subtitle color, and font size for dataset information
    st.markdown(
        """
        <style>
        .main {
            background-color: #000000; /* Light blue background */
        }
        h1 {
            font-family: 'Verdana', sans-serif;
            font-size: 50px;
            color: #3b64ff; /* Dark blue color for the main title */
            text-align: center; /* Center the main title */
        }
        h2 {
            color: #464646; /* Gray color for subtitles */
        }
        .dataset-info {
            font-size: 18px; /* Font size for dataset information */
            color: #707070; /* Dark grey for contrast */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Page content
    st.title("MBA Admission Predictor - Wharton University")
    st.image("wharton_image", use_column_width=True)  

    st.subheader("Introduction")
    st.markdown("""
    This project aims to develop an Artificial Neural Network model to **predict admission outcomes** for MBA candidates at Wharton University.
    
    In the following page you will find the predictor page that a potential student can use to input its own information and see his chances to be admitted into the program.
    """)

    st.subheader("About the Dataset")
    st.image("dataset.jpg", use_column_width=True)  

    st.write("**Data Source:** Synthetic data generated from the Wharton Class of 2025's statistics.")
    
    st.write("**Features in the dataset:**")
    st.markdown("""
    - **`application_id`**: Unique identifier for each application
    - **`gender`**: Applicant's gender (Male, Female)
    - **`international`**: International student (TRUE/FALSE)
    - **`gpa`**: Grade Point Average of the applicant (on 4.0 scale)
    - **`major`**: Undergraduate major (Business, STEM, Humanities)
    - **`race`**: Racial background of the applicant (e.g., White, Black, Asian, Hispanic, Other / null for international students)
    - **`gmat`**: GMAT score of the applicant (max 800 points)
    - **`work_exp`**: Number of years of work experience
    - **`work_industry`**: Industry of the applicant's previous work experience (e.g., Consulting, Finance, Technology, etc.)
    - **`admission`**: Admission status (Admit, Waitlist, Null: Deny)
    """)

    st.write("[Link to the dataset](https://www.kaggle.com/datasets/taweilo/mba-admission-dataset)")

    st.markdown('''
        For more information on the training of the model, please refer to the comments in the code.
        ''')

# Display the introduction page
introduction_page()
