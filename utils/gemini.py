import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_resume(resume_text):

    prompt = f"""
Analyze this resume and provide:
1. Professional Summary
2. Skills Found
3. Missing Skills
4. Suggested Job Roles
5. Resume Improvement Tips

Resume:
{resume_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        error_msg = str(e)
        if "quota" in error_msg.lower() or "429" in error_msg:
            return "⚠️ Gemini API Quota Exceeded!\n\nPlease try again later or use a different API key. In the meantime, check out our fallback analysis below!"
        else:
            return f"⚠️ Gemini AI Error: {error_msg}"