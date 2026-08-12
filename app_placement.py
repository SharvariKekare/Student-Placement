import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("placement_package_prediction_model.pkl")

st.title("Student Placement Package Prediction")

# Dropdown Inputs
student_id = st.selectbox("Student ID", range(1,10001))

cgpa = st.selectbox("CGPA", [round(i*0.1,1) for i in range(50,101)])

internships = st.selectbox("Internships", range(0,11))

projects = st.selectbox("Projects", range(0,11))

workshops = st.selectbox("Workshops / Certifications", range(0,11))

aptitude = st.selectbox("Aptitude Test Score", range(0,101))

softskills = st.selectbox("Soft Skills Rating",
                          [round(i*0.5,1) for i in range(0,21)])

extra = st.selectbox("Extracurricular Activities", ["No","Yes"])

training = st.selectbox("Placement Training", ["No","Yes"])

ssc = st.selectbox("SSC Marks", range(35,101))

hsc = st.selectbox("HSC Marks", range(35,101))

# Convert Yes/No to 0/1
extra = 1 if extra == "Yes" else 0
training = 1 if training == "Yes" else 0

# Experience Score
experience = internships + projects + workshops

# Predict
if st.button("Predict Package"):

    input_data = pd.DataFrame({
        "StudentID":[student_id],
        "CGPA":[cgpa],
        "Internships":[internships],
        "Projects":[projects],
        "Workshops_Certifications":[workshops],
        "AptitudeTestScore":[aptitude],
        "SoftSkillsRating":[softskills],
        "ExtracurricularActivities":[extra],
        "PlacementTraining":[training],
        "SSC_Marks":[ssc],
        "HSC_Marks":[hsc],
        "ExperienceScore":[experience]
    })

    prediction = model.predict(input_data)

    st.success(f"Expected Salary Package: {prediction[0]:.2f} LPA")