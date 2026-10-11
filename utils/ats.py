import re

REQUIRED_SKILLS = [
    "python",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "django",
    "flask",
    "machine learning",
    "git"
]

def calculate_ats_score(resume_text):

    resume = resume_text.lower()

    found = []

    missing = []

    for skill in REQUIRED_SKILLS:

        if re.search(skill, resume):
            found.append(skill)
        else:
            missing.append(skill)

    score = int((len(found) / len(REQUIRED_SKILLS)) * 100)

    return score, found, missing