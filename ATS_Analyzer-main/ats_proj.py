#importing neccessary libraries
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv
load_dotenv()

#api key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

#initilizig model
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content(input)
    return response.text

#uploading file
def input_pdf_text(uploaded_file):
    file=pdf.PdfReader(uploaded_file)
    text=""
    for page_no in range(len(file.pages)):
        page=file.pages[page_no]
        text+=str(page.extract_text())
    return text

#prompt_template
input_prompt='''
Act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of tech field, software engineering, data science, data analyst and big data engineer. Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide best assistance for improving the resumes. Assign the percentage Matching based on Jd and the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in one single string having the structure \
{{"JD Match":"%", 
"Missing Keywords : []",
"Profile Summary" : ""}}
'''
#streamlit
st.set_page_config(page_title="🚀 ATS Resume Tracker")
st.title("📄 ATS Resume Checker")
st.header("Increase the chance to secure your dream job", divider="gray")
jd=st.text_area("Paste Job desciption")

#sidebar
st.sidebar.markdown(" 📝 Instructions")
st.sidebar.markdown("""
    **How to use:**
    1. Upload the PDF document using the upload button below.
    2. Ensure that your document is in PDF format.

"""
)

uploaded_file=st.sidebar.file_uploader("Upload your resume", type="pdf",
                                 help="Please upload the pdf")

submit=st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)      