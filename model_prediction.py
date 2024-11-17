import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def predictor_page():
    # Load the trained model
    pickle_in = open("Predictor1.pkl", 'rb')  # Replace with the correct model path
    classifier = pickle.load(pickle_in)

    # Load dataset to fit the scaler and encoder
    df = pd.read_csv('MBA.csv')

    # Preprocess the dataset
    df = df.dropna()  # Drop missing values for simplicity

    # Separate target and features
    X = df.drop(columns="admission")
    y = df["admission"]

    # Split dataset for preprocessing
    X_train, _, _, _ = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

    # Separate categorical and numerical features
    categorical_columns = ["gender", "major", "race", "work_industry"]
    numerical_columns = ["gpa", "gmat", "work_exp"]

    X_train_cat = X_train[categorical_columns]
    X_train_num = X_train[numerical_columns]

    # Fit and transform numerical features
    sc = StandardScaler()
    sc.fit(X_train_num)

    # Fit and transform categorical features
    ohe = OneHotEncoder(sparse_output=False)
    ohe.fit(X_train_cat)

    # Function to preprocess a single sample
    def preprocess_sample(sample):
        categorical_features = pd.DataFrame([[sample[col] for col in categorical_columns]],
                                             columns=categorical_columns)
        cat_features_encoded = ohe.transform(categorical_features)
        cat_features_encoded = pd.DataFrame(cat_features_encoded, columns=ohe.get_feature_names_out())

        numerical_features = np.array([[sample[col] for col in numerical_columns]])
        num_features_scaled = sc.transform(numerical_features)
        num_features_scaled = pd.DataFrame(num_features_scaled, columns=numerical_columns)

        final_sample = pd.concat([cat_features_encoded, num_features_scaled], axis=1)
        return final_sample

    # Function to predict admission
    def prediction(sample):
        processed_sample = preprocess_sample(sample)
        pred = classifier.predict(processed_sample)
        return "🎉 Admitted!" if pred > 0.05 else "❌ Rejected"

    # Streamlit UI
    st.markdown('<div style="text-align: center;"><h1>🎓 MBA Admission Predictor</h1></div>', unsafe_allow_html=True)

    st.header("📋 Enter Applicant Details")
    gender = st.selectbox('Gender', df["gender"].unique())
    gpa = st.number_input("📘 GPA (out of 4.0)", min_value=0.0, max_value=4.0, step=0.1)
    gmat = st.number_input("📊 GMAT Score", min_value=200, max_value=800, step=10)
    work_exp = st.number_input("💼 Work Experience (years)", min_value=0, step=1)
    major = st.selectbox('📚 Major', df["major"].unique())
    race = st.selectbox('🌍 Racial Background', df["race"].unique())
    work_industry = st.selectbox('🏢 Work Industry', df["work_industry"].unique())

    if st.button("🔍 Predict"):
        sample = {
            "gender": gender,
            "gpa": gpa,
            "gmat": gmat,
            "work_exp": work_exp,
            "major": major,
            "race": race,
            "work_industry": work_industry
        }
        result = prediction(sample)
        st.success(f'Your admission status is: {result}')

# To test the page, ensure you call the function appropriately within the Streamlit app setup
