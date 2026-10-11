import re

def extract_resume_info(text):

    info = {}

    # ----------------------------------
    # Clean Text
    # ----------------------------------

    text = text.strip()

    lines = []

    for line in text.split("\n"):

        line = line.strip()

        if line:
            lines.append(line)

    # ----------------------------------
    # Email
    # ----------------------------------

    email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    info["Email"] = email[0] if email else "Not Found"

    # ----------------------------------
    # Phone Number
    # ----------------------------------

    phone = re.findall(r'(\+?\d[\d\s\-]{8,}\d)', text)

    info["Phone"] = phone[0] if phone else "Not Found"

    # ----------------------------------
    # Name
    # ----------------------------------

    ignore_words = [
        "resume",
        "curriculum",
        "vitae",
        "email",
        "phone",
        "contact"
    ]

    name = "Not Found"

    for line in lines:

        if (
            len(line.split()) <= 4
            and not any(word.lower() in line.lower() for word in ignore_words)
            and "@" not in line
            and not any(char.isdigit() for char in line)
        ):
            name = line
            break

    info["Name"] = name

    # ----------------------------------
    # Education
    # ----------------------------------

    education = []

    keywords = [
        "B.Tech",
        "B.E",
        "M.Tech",
        "M.E",
        "Bachelor",
        "Master",
        "Engineering",
        "College",
        "University",
        "Information Technology",
        "Computer Science",
        "Electronics",
        "Mechanical",
        "Civil"
    ]

    for line in lines:

        if any(keyword.lower() in line.lower() for keyword in keywords):

            if line not in education:
                education.append(line)

    info["Education"] = list(dict.fromkeys(education))

    return info