pip install -r requirements.txt
import spacy
import streamlit as st
from pdfminer.high_level import extract_text

# Load the trained NER model
model = spacy.load("/content/drive/MyDrive/Custom_NER/output/model-best")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

# Function to parse resume using the NER model
def parse_resume(text):
    doc = model(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

# Streamlit App
st.title("Resume Parser")

# File uploader for resume in PDF format
uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file is not None:
    # Extract text from the uploaded PDF file
    resume_text = extract_text_from_pdf(uploaded_file)

    st.write("### Extracted Text")
    st.write(resume_text)

    # Parse the resume using the NER model
    parsed_info = parse_resume(resume_text)

    st.write("### Parsed Information")
    for entity, label in parsed_info:
        st.write(f"{label}: {entity}")
