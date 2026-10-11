from utils.pdf_reader import extract_text_from_pdf
from utils.gemini import analyze_resume
from utils.ats import calculate_ats_score
from utils.extractor import extract_resume_info
from utils.job_recommender import recommend_jobs
from utils.pdf_report import generate_pdf
import matplotlib.pyplot as plt
import streamlit as st
from utils.matcher import match_resume_with_job
# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------------------------------
# Tailwind CSS CDN
# ---------------------------------------
st.markdown("""
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.1/dist/tailwind.min.css" rel="stylesheet">
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    [data-testid="stFileUploadDropzone"] {
        border: 2px dashed #3b82f6;
        border-radius: 0.75rem;
        padding: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------
# Sidebar
# ---------------------------------------
with st.sidebar:
    st.markdown('<div class="p-4 bg-blue-50 rounded-xl mb-4">', unsafe_allow_html=True)
    st.title("📌 AI Resume Analyzer")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Built With")
    st.markdown("""
    <ul class="mt-2 space-y-1">
        <li class="flex items-center gap-2">
            <span class="text-blue-600">•</span> Python
        </li>
        <li class="flex items-center gap-2">
            <span class="text-blue-600">•</span> Streamlit
        </li>
        <li class="flex items-center gap-2">
            <span class="text-blue-600">•</span> Gemini AI
        </li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("### ✨ Features")
    st.markdown("""
    <ul class="mt-2 space-y-1">
        <li class="flex items-center gap-2">
            <span class="text-green-600">✅</span> ATS Score
        </li>
        <li class="flex items-center gap-2">
            <span class="text-green-600">✅</span> Skills Analysis
        </li>
        <li class="flex items-center gap-2">
            <span class="text-green-600">✅</span> Job Recommendations
        </li>
        <li class="flex items-center gap-2">
            <span class="text-green-600">✅</span> Resume Reports
        </li>
    </ul>
    """, unsafe_allow_html=True)

# ---------------------------------------
# Title
# ---------------------------------------

st.markdown('<div class="text-center mb-8">', unsafe_allow_html=True)
st.title("📄 AI Resume Analyzer")
st.subheader("Analyze Your Resume Using Artificial Intelligence")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="bg-blue-50 border border-blue-200 rounded-2xl p-6 mb-8">
    <h4 class="text-xl font-semibold text-blue-800 mb-3">What you'll get:</h4>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div class="flex items-center gap-2 text-gray-700">
            <span class="text-green-600 text-lg">✅</span> ATS Score
        </div>
        <div class="flex items-center gap-2 text-gray-700">
            <span class="text-green-600 text-lg">✅</span> Resume Information Extraction
        </div>
        <div class="flex items-center gap-2 text-gray-700">
            <span class="text-green-600 text-lg">✅</span> Skills Analysis
        </div>
        <div class="flex items-center gap-2 text-gray-700">
            <span class="text-green-600 text-lg">✅</span> Missing Skills Identification
        </div>
        <div class="flex items-center gap-2 text-gray-700">
            <span class="text-green-600 text-lg">✅</span> Career Recommendations
        </div>
        <div class="flex items-center gap-2 text-gray-700">
            <span class="text-green-600 text-lg">✅</span> Resume Improvement Suggestions
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------
# Upload Resume
# ---------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Your Resume (PDF)",
    type=["pdf"]
)
if uploaded_file:

    st.markdown('<div class="bg-green-50 border border-green-200 rounded-xl p-4 mb-4">', unsafe_allow_html=True)
    st.success("✅ Resume uploaded successfully!")
    st.write(f"**Filename:** {uploaded_file.name}")
    st.markdown('</div>', unsafe_allow_html=True)


    if st.button("🤖 Analyze Resume"):
    # Extract Resume
        resume_text = extract_text_from_pdf(uploaded_file)
        info = extract_resume_info(resume_text)

        score, skills, missing = calculate_ats_score(resume_text)

        jobs = recommend_jobs(skills)

        if score >= 90:
           rating = "🌟 Excellent Resume"
        elif score >= 70:
           rating = "👍 Good Resume"
        elif score >= 50:
           rating = "⚠ Average Resume"
        else:
           rating = "❌ Resume Needs Improvement"

        try:
            analysis = analyze_resume(resume_text)
        except Exception as e:
            analysis = "⚠️ Gemini AI is currently unavailable."
            st.warning(str(e))
    # Create Tabs
        tab1, tab2, tab3, tab4 = st.tabs([
           "📄 Resume Analysis",
           "📊 Dashboard",
           "🎯 Job Match",
           "📥 Download Report"
        ])
    # ====================================================
    # TAB 1 - Resume Analysis
    # ====================================================

        with tab1:

            st.header("📄 Resume Analysis")

        # ------------------------------------
        # Resume Length
        # ------------------------------------

            st.markdown("""
            <div class="bg-gray-50 rounded-xl p-4 mb-4">
                <h4 class="text-lg font-semibold text-gray-700 mb-2">📏 Resume Length</h4>
                <div class="text-2xl font-bold text-blue-600">{} Characters</div>
            </div>
            """.format(len(resume_text)), unsafe_allow_html=True)

            st.divider()

        # ------------------------------------
        # Resume Information
        # ------------------------------------

            st.subheader("👤 Resume Information")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="bg-green-50 border border-green-200 rounded-xl p-4 mb-4">', unsafe_allow_html=True)
                st.markdown("<h5 class='text-green-700 font-semibold mb-2'>👤 Name</h5>", unsafe_allow_html=True)
                st.markdown(f"<p class='text-lg font-medium'>{info['Name']}</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="bg-green-50 border border-green-200 rounded-xl p-4">', unsafe_allow_html=True)
                st.markdown("<h5 class='text-green-700 font-semibold mb-2'>📧 Email</h5>", unsafe_allow_html=True)
                st.markdown(f"<p class='text-lg font-medium'>{info['Email']}</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="bg-green-50 border border-green-200 rounded-xl p-4">', unsafe_allow_html=True)
                st.markdown("<h5 class='text-green-700 font-semibold mb-2'>📞 Phone</h5>", unsafe_allow_html=True)
                st.markdown(f"<p class='text-lg font-medium'>{info['Phone']}</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("<h5 class='text-lg font-semibold text-gray-700 mt-6 mb-3'>🎓 Education</h5>", unsafe_allow_html=True)

            if info["Education"]:
                st.markdown('<div class="space-y-2">', unsafe_allow_html=True)
                for edu in info["Education"]:
                    st.markdown(f'<div class="bg-green-50 border border-green-200 rounded-lg p-3">{edu}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Education not found.")

            st.divider()

        # ------------------------------------
        # Resume Text
        # ------------------------------------

            st.subheader("📄 Extracted Resume Text")
            st.text_area(
                "Resume Content",
                resume_text,
                height=250
            )
            st.divider()

        # ------------------------------------
        # ATS Score
        # ------------------------------------

            st.subheader("⭐ ATS Score")
            score_col1, score_col2 = st.columns([1, 3])
            with score_col1:
                st.metric(
                    "Resume Score",
                    f"{score}/100"
                )
            with score_col2:
                st.progress(score / 100)
            st.divider()

        # ------------------------------------
        # Skills Found
        # ------------------------------------

            st.subheader("🛠 Skills Found")
            if skills:
                st.markdown('<div class="flex flex-wrap gap-2">', unsafe_allow_html=True)
                for skill in skills:
                    st.markdown(f'<span class="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium">✔ {skill.title()}</span>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("No required skills found.")
            st.divider()

        # ------------------------------------
        # Missing Skills
        # ------------------------------------

            st.subheader("❌ Missing Skills")
            if missing:
                st.markdown('<div class="flex flex-wrap gap-2">', unsafe_allow_html=True)
                for skill in missing:
                    st.markdown(f'<span class="bg-red-100 text-red-800 px-3 py-1 rounded-full text-sm font-medium">✖ {skill.title()}</span>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.success("🎉 Excellent! No important skills are missing.")
            st.divider()

        # ------------------------------------
        # Recommended Jobs
        # ------------------------------------

            st.subheader("💼 Recommended Job Roles")
            st.markdown('<div class="grid grid-cols-1 md:grid-cols-2 gap-3">', unsafe_allow_html=True)
            for job in jobs:
                st.markdown(f'<div class="bg-blue-50 border border-blue-200 rounded-lg p-4">{job}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            st.divider()

        # ------------------------------------
        # Resume Rating
        # ------------------------------------

            st.subheader("📊 Resume Rating")
            if score >= 90:
                st.markdown(f'<div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-xl font-semibold text-lg">{rating}</div>', unsafe_allow_html=True)
            elif score >= 70:
                st.markdown(f'<div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded-xl font-semibold text-lg">{rating}</div>', unsafe_allow_html=True)
            elif score >= 50:
                st.markdown(f'<div class="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded-xl font-semibold text-lg">{rating}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-xl font-semibold text-lg">{rating}</div>', unsafe_allow_html=True)
            st.divider()

        # ------------------------------------
        # AI Analysis
        # ------------------------------------

            st.subheader("🤖 AI Resume Analysis")
            if analysis.startswith("⚠️"):
                st.warning(analysis)
                st.markdown("""
                <div class="bg-blue-50 border border-blue-200 rounded-xl p-4 mt-4">
                    <h4 class="text-blue-800 font-semibold mb-2">📋 Fallback Analysis (Without AI)</h4>
                    <ul class="mt-2 space-y-1 text-gray-700">
                        <li><strong>Professional Summary:</strong> Based on your skills, you're a motivated individual with strong technical skills looking for opportunities in software development or AI/ML.</li>
                        <li><strong>Skills Found:</strong> {skills_str}</li>
                        <li><strong>Missing Skills:</strong> {missing_str}</li>
                        <li><strong>Resume Improvement Tips:</strong> Add more project details with metrics, include work experience (if any), and highlight soft skills with examples.</li>
                    </ul>
                </div>
                """.format(
                    skills_str=", ".join([skill.title() for skill in skills]),
                    missing_str=", ".join([skill.title() for skill in missing]) if missing else "None - Great job!"
                ), unsafe_allow_html=True)
            else:
                st.write(analysis)
        # ====================================================
        # TAB 2 - Dashboard
        # ====================================================

        with tab2:

            st.header("📊 Dashboard")
            
            # Metrics row first
            st.subheader("📋 Resume Statistics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('<div class="bg-gray-50 border border-gray-200 rounded-xl p-4">', unsafe_allow_html=True)
                st.metric("Skills Found", len(skills))
                st.markdown('</div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="bg-gray-50 border border-gray-200 rounded-xl p-4">', unsafe_allow_html=True)
                st.metric("Missing Skills", len(missing))
                st.markdown('</div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="bg-gray-50 border border-gray-200 rounded-xl p-4">', unsafe_allow_html=True)
                st.metric("ATS Score", f"{score}%")
                st.markdown('</div>', unsafe_allow_html=True)
            st.divider()
            
            # Resume performance
            st.subheader("🏆 Resume Performance")
            if score >= 90:
                st.markdown('<div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-xl font-semibold text-lg">🌟 Excellent Resume</div>', unsafe_allow_html=True)
            elif score >= 70:
                st.markdown('<div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded-xl font-semibold text-lg">👍 Good Resume</div>', unsafe_allow_html=True)
            elif score >= 50:
                st.markdown('<div class="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded-xl font-semibold text-lg">⚠ Average Resume</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-xl font-semibold text-lg">❌ Resume Needs Improvement</div>', unsafe_allow_html=True)
            st.divider()

        # ------------------------------------
        # Charts
        # ------------------------------------
            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                st.subheader("🥧 Skills Distribution")
                labels = ["Skills Found", "Missing Skills"]
                values = [len(skills), len(missing)]
                fig1, ax1 = plt.subplots(figsize=(4, 4))
                ax1.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=['#4ade80', '#f87171'])
                ax1.axis("equal")
                st.pyplot(fig1)
            
            with chart_col2:
                st.subheader("📈 Skills Found Chart")
                if skills:
                    fig2, ax2 = plt.subplots(figsize=(4, 4))
                    ax2.bar(skills, [1]*len(skills), color="#3b82f6")
                    plt.xticks(rotation=45, ha='right')
                    ax2.set_xlabel("Skills")
                    ax2.set_ylabel("Found")
                    ax2.set_title("Detected Skills")
                    plt.tight_layout()
                    st.pyplot(fig2)
            st.divider()
                
        # ====================================================
        # TAB 3 - Job Match
        # ====================================================

        with tab3:

            st.header("🎯 Resume vs Job Description")

            st.subheader("📋 Job Description")

            job_description = st.text_area(
                "Paste the Job Description Here",
                height=220
            )

            if job_description.strip():

               match_score, matched_skills, missing_job_skills = match_resume_with_job(
                   resume_text,
                   job_description
               )

               st.divider()

               st.subheader("🎯 ATS Match Score")
               match_col1, match_col2 = st.columns([1, 3])
               with match_col1:
                   st.metric(
                        "Resume Match",
                        f"{match_score}%"
                   )
               with match_col2:
                   st.progress(match_score / 100)

               st.divider()

               st.subheader("✅ Matched Keywords")
               if matched_skills:
                   st.markdown('<div class="flex flex-wrap gap-2">', unsafe_allow_html=True)
                   for skill in sorted(matched_skills):
                       st.markdown(f'<span class="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium">✔ {skill.title()}</span>', unsafe_allow_html=True)
                   st.markdown('</div>', unsafe_allow_html=True)
               else:
                   st.warning("No matching keywords found.")

               st.divider()

               st.subheader("❌ Missing Keywords")
               if missing_job_skills:
                   st.markdown('<div class="flex flex-wrap gap-2">', unsafe_allow_html=True)
                   for skill in sorted(missing_job_skills):
                       st.markdown(f'<span class="bg-red-100 text-red-800 px-3 py-1 rounded-full text-sm font-medium">✖ {skill.title()}</span>', unsafe_allow_html=True)
                   st.markdown('</div>', unsafe_allow_html=True)
               else:
                   st.success("Excellent! No keywords are missing.")

            else:

                st.info("📋 Paste a Job Description to compare with your resume.")
        
            
        # ====================================================
        # TAB 4 - Download Report
        # ====================================================

        with tab4:

            st.header("📥 Download Resume Report")

            st.markdown("""
            <div class="bg-blue-50 border border-blue-200 rounded-xl p-6 mb-6">
                <p class="text-gray-700">Download the complete AI Resume Analysis Report as a PDF for your records.</p>
            </div>
            """, unsafe_allow_html=True)
            st.divider()

        # ----------------------------------------
        # Generate PDF Report
        # ----------------------------------------

            generate_pdf(
                "report/resume_report.pdf",
                info,
                score,
                skills,
                missing,
                jobs,
                rating,
                analysis
            )

            st.markdown('<div class="bg-green-50 border border-green-200 rounded-xl p-4 mb-4">', unsafe_allow_html=True)
            st.success("✅ PDF Report Generated Successfully!")
            st.markdown('</div>', unsafe_allow_html=True)

        # ----------------------------------------
        # Download Button
        # ----------------------------------------

            with open("report/resume_report.pdf", "rb") as pdf_file:
                st.download_button(
                    label="📄 Download AI Resume Report",
                    data=pdf_file,
                    file_name="AI_Resume_Report.pdf",
                    mime="application/pdf"
                )    
            
    # ----------------------------------------------------
    # End of if st.button()
    # ----------------------------------------------------

else:
    st.markdown("""
    <div class="text-center p-10 bg-gray-50 rounded-2xl">
        <div class="text-5xl mb-4">📂</div>
        <h3 class="text-2xl font-semibold text-gray-700 mb-2">Please Upload Your Resume</h3>
        <p class="text-gray-500">Upload a PDF resume to start the analysis.</p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.divider()

st.markdown(
    """
    <div class="text-center py-6 text-gray-500">
        <h4 class="text-xl font-semibold mb-2 text-gray-700">📄 AI Resume Analyzer</h4>
        <p class="mb-1">Developed using Python • Streamlit • Gemini AI</p>
        <p class="font-semibold text-gray-600">Created by Jenika K</p>
    </div>
    """,
    unsafe_allow_html=True
)        