import re

def match_resume_with_job(resume_text, job_description):

    resume = resume_text.lower()
    job = job_description.lower()

    # Extract unique words
    resume_words = set(re.findall(r"\b[a-zA-Z]+\b", resume))
    job_words = set(re.findall(r"\b[a-zA-Z]+\b", job))

    matched = resume_words.intersection(job_words)
    missing = job_words - resume_words

    if len(job_words) == 0:
        score = 0
    else:
        score = int((len(matched) / len(job_words)) * 100)

    return score, sorted(matched), sorted(missing)