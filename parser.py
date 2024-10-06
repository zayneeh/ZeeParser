pip install -r requirements.txt 
import streamlit as st
import spacy
import PyPDF2
import docx2txt  # For reading .docx files

# Load your spaCy model
nlp = spacy.load("path/to/your/model")

# Title of the app
st.title("NLP Resume Parsing App")

# File uploader for multiple file types
uploaded_file = st.file_uploader("Upload a Resume", type=["pdf", "docx", "txt"])

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  # Adding fallback for non-text pages
    return text

# Function to extract text from DOCX using python-docx
def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

# Function to extract text from TXT files
def extract_text_from_txt(txt_file):
    return txt_file.read().decode("utf-8")

# Process the uploaded file
if uploaded_file is not None:
    file_type = uploaded_file.type

    # Handle different file types
    if file_type == "application/pdf":
        with st.spinner("Extracting text from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
            extracted_text = pdf_text

    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        with st.spinner("Extracting text from DOCX..."):
            docx_text = extract_text_from_docx(uploaded_file)
            extracted_text = docx_text

    elif file_type == "text/plain":
        with st.spinner("Extracting text from TXT file..."):
            txt_text = extract_text_from_txt(uploaded_file)
            extracted_text = txt_text

    else:
        st.error("Unsupported file type!")
        extracted_text = None

    # Display the extracted text if available
    if extracted_text:
        st.subheader("Extracted Text from File:")
        st.write(extracted_text)

        # Button to parse the text
        if st.button("Parse"):
            with st.spinner("Parsing text..."):
                doc = nlp(extracted_text)

                # Display extracted entities in a cleaner format
                st.subheader("Extracted Entities:")
                data = [{"Entity": ent.text, "Type": ent.label_} for ent in doc.ents]
                st.dataframe(data)
    else:
        st.error("No text could be extracted from the uploaded file.")
