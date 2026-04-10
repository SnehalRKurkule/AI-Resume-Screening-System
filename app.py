import streamlit as st
import pandas as pd

from utils.parser import extract_text
from utils.nlp import clean_text, extract_skills
from utils.matching import get_similarity



st.title("AI Resume Screening System (BERT + Skill Matching)")

jd = st.text_area("Enter Job Description")
uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True)

results = []

if uploaded_files and jd:
    jd_clean = clean_text(jd)
    jd_skills = extract_skills(jd)

    for file in uploaded_files:
        text = extract_text(file)
        clean = clean_text(text)

        # Extract skills from resume
        resume_skills = extract_skills(text)

        # 🔹 1. BERT Similarity
        similarity = get_similarity(clean, jd_clean)

        # 🔹 2. Skill Matching Score
        matched_skills = set(jd_skills) & set(resume_skills)

        if len(jd_skills) > 0:
            skill_score = len(matched_skills) / len(jd_skills)
        else:
            skill_score = 0

        # 🔹 3. FINAL SCORE 
        final_score = (0.6 * similarity) + (0.4 * skill_score)

        results.append({
            "Resume": file.name,
            "Skills": ", ".join(resume_skills),
            "Matched Skills": ", ".join(matched_skills),
            "Similarity": round(similarity, 2),
            "Skill Score": round(skill_score, 2),
            "Score": round(final_score, 2)
        })

    df = pd.DataFrame(results)
    df = df.sort_values(by="Score", ascending=False)

    st.subheader("Ranked Candidates")
    st.dataframe(df)