# AI Resume Analyzer

A Python-based web application that analyzes resumes, identifies skills, calculates a simplified Applicant Tracking System (ATS) score, recommends career options, and generates downloadable PDF reports.

## Features

- **Resume Analysis:** Extracts text and relevant information from PDF resumes.
- **ATS Score:** Calculates a skill-matching score using predefined skills.
- **Skills Analysis:** Identifies available and missing technical skills.
- **Job Recommendations:** Suggests potential career options based on resume skills.
- **Gemini AI Integration:** Supports AI-powered resume feedback when API access is available.
- **PDF Report:** Generates a downloadable resume analysis report.
- **Interactive Dashboard:** Provides an easy-to-use interface built with Streamlit.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- pdfplumber
- ReportLab
- python-dotenv

## Installation and Setup

1. Clone this repository.
2. Open the project folder in VS Code.
3. Create a virtual environment:

   `python -m venv venv`

4. Activate the environment on Windows:

   `venv\Scripts\activate`

5. Install dependencies:

   `pip install -r requirements.txt`

6. Configure your Gemini API key in a local `.env` file using the environment variable expected by the application.

7. Run the application:

   `streamlit run app.py`

## How It Works

1. Upload a PDF resume.
2. Extract text from the document.
3. Identify resume details and technical skills.
4. Calculate the predefined skill-matching score.
5. Review career recommendations and available AI feedback.
6. Download the generated PDF report.

## Limitations

The ATS score is a simplified skill-matching indicator, not a complete commercial ATS evaluation. Gemini AI features depend on API configuration, availability, and quota. Scanned PDFs may require OCR support.

## Security

Never upload API keys, private resumes, or other confidential information to a public repository.

## Author

**Jenika K**

GitHub: [Jenika-2307](https://github.com/Jenika-2307)