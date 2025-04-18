# ATS Resume Checker

This Streamlit application allows users to analyze resumes against job descriptions, helping optimize resumes for ATS (Applicant Tracking Systems) by providing a match percentage, missing keywords, and a profile summary.

The application uses Google Generative AI for analysis, PyPDF2 for PDF processing, and Streamlit for the interactive interface.

---

## Features

- **Resume Upload**: Upload resumes in PDF format.
- **Job Description Input**: Enter job descriptions to compare against the resume.
- **ATS Analysis**: Provides a percentage match, missing keywords, and a profile summary.
- **Interactive UI**: Built with Streamlit for a user-friendly experience.
- **AI-Powered Insights**: Uses Google Generative AI to evaluate resumes.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher  
- Streamlit  
- PyPDF2  
- Google Generative AI  
- python-dotenv  

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TahaNadeemkhan/ATS_Analyzer-main.git
   cd ATS_Analyzer-main
   ```

2. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:

   Create a `.env` file in the root directory and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Run the Streamlit application**:
   ```bash
   python -m streamlit run ats_proj.py
   ```

---

## Project Tags

`Ats_resume_Analyzer` `ATS` `Streamlit` `Resume Analyzer` `Generative AI`
