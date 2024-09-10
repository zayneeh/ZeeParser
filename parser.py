pip install -r requirements.txt
import streamlit as st
import spacy
import PyPDF2

# Load your spaCy model
nlp = spacy.load("path_to_your_model")

# Title of the app
st.title("NLP Resume Parsing App")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload a PDF Resume", type="pdf")

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Process the uploaded file
if uploaded_file is not None:
    # Extract text from the uploaded PDF
    pdf_text = extract_text_from_pdf(uploaded_file)
    
    # Display the extracted text
    st.subheader("Extracted Text from PDF:")
    st.write(pdf_text)

    # Button to parse the text
    if st.button("Parse"):
        doc = nlp(pdf_text)
        
        # Display extracted entities
        st.subheader("Extracted Entities:")
        for ent in doc.ents:
            st.write(f"{ent.text} ({ent.label_})")
