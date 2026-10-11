from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    info,
    score,
    skills,
    missing,
    jobs,
    rating,
    analysis
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Name:</b> {info['Name']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Email:</b> {info['Email']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Phone:</b> {info['Phone']}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}/100", styles["BodyText"]))

    story.append(Paragraph(f"<b>Resume Rating:</b> {rating}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Skills Found</b>", styles["Heading2"]))

    for skill in skills:
        story.append(Paragraph("• " + skill.title(), styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    if missing:
        for skill in missing:
            story.append(Paragraph("• " + skill.title(), styles["BodyText"]))
    else:
        story.append(Paragraph("No Missing Skills", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Recommended Jobs</b>", styles["Heading2"]))

    for job in jobs:
        story.append(Paragraph(job, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>AI Analysis</b>", styles["Heading2"]))

    story.append(Paragraph(analysis.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)
    