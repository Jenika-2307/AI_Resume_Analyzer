def recommend_jobs(skills):

    jobs = []

    skills = [skill.lower() for skill in skills]

    # Python Developer
    if "python" in skills:
        jobs.append("🐍 Python Developer")

    # Web Developer
    if "html" in skills and "css" in skills and "javascript" in skills:
        jobs.append("🌐 Web Developer")

    # Full Stack Developer
    if (
        "html" in skills and
        "css" in skills and
        "javascript" in skills and
        "react" in skills
    ):
        jobs.append("💻 Full Stack Developer")

    # Django Developer
    if "django" in skills:
        jobs.append("🚀 Django Developer")

    # Flask Developer
    if "flask" in skills:
        jobs.append("⚡ Flask Developer")

    # AI Engineer
    if "machine learning" in skills:
        jobs.append("🤖 AI Engineer")

    # Machine Learning Engineer
    if (
        "machine learning" in skills and
        "python" in skills
    ):
        jobs.append("🧠 Machine Learning Engineer")

    # Data Analyst
    if (
        "python" in skills and
        "sql" in skills
    ):
        jobs.append("📊 Data Analyst")

    # Software Engineer
    if len(skills) >= 5:
        jobs.append("💼 Software Engineer")

    if not jobs:
        jobs.append("🎯 Fresher / Internship Opportunities")

    return jobs