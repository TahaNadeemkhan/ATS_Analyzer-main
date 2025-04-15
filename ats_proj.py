import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re

load_dotenv()

try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    st.error("Google API key not found. Please set GOOGLE_API_KEY in your .env file.")
    st.stop()

def get_gemini_response(input_text):
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(input_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        if not text.strip():
            st.warning("No text extracted from the PDF.")
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

input_prompt = '''
Act like a skilled ATS with deep understanding of tech fields (software engineering, data science, data analyst, big data engineer). 
Evaluate the resume based on the job description. Consider a competitive job market and provide suggestions for improving the resume. 
Assign a percentage match based on the JD and identify missing keywords with high accuracy.

Resume: {text}
Job Description: {jd}

Return the response strictly as a JSON string in the following format. Do not include any additional text, explanations, suggestions, Markdown, asterisks, or formatting outside the JSON. The response must be a valid JSON string only:
{{"JD Match":"%", "Missing Keywords": [], "Profile Summary": ""}}
'''

st.set_page_config(page_title="ATS Resume Tracker")
st.title("ATS Resume Checker")
st.header("Increase the chance to secure your dream job", divider="gray")

jd = st.text_area("Paste Job Description", height=200)

st.sidebar.markdown("📝 Instructions")
st.sidebar.markdown("""
    **How to use:**
    1. Upload your resume in PDF format.
    2. Paste the job description in the text area.
    3. Click Submit to analyze.
""")

uploaded_file = st.sidebar.file_uploader("Upload your resume", type="pdf", help="Please upload a PDF file.")

submit = st.button("Submit")

if submit:
    if not uploaded_file:
        st.error("Please upload a resume.")
    elif not jd.strip():
        st.error("Please provide a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            resume_text = input_pdf_text(uploaded_file)
            if resume_text:
                formatted_prompt = input_prompt.format(text=resume_text, jd=jd)
                response = get_gemini_response(formatted_prompt)
                if response:
                    try:
                        # Clean the response to extract only the JSON
                        json_match = re.search(r'\{.*\}', response, re.DOTALL)
                        if json_match:
                            response_json = json_match.group(0)
                            response_dict = json.loads(response_json)
                            st.subheader("ATS Analysis Results")
                            st.write(f"**JD Match**: {response_dict['JD Match']}")
                            st.write(f"**Missing Keywords**: {', '.join(response_dict['Missing Keywords']) or 'None'}")
                            st.write(f"**Profile Summary**: {response_dict['Profile Summary']}")
                        else:
                            st.error("Could not extract valid JSON from response.")
                            st.write("Raw response:", response)
                    except json.JSONDecodeError:
                        st.error("Invalid response format.")
                        st.write("Raw response:", response)