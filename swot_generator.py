def perform_swot_analysis(profile: dict) -> dict:
    swot = {'strengths': [], 'weaknesses': [], 'opportunities': [], 'threats': []}

    # Fetch values from profile
    name = profile.get("name", "")
    age = profile.get("age", "")
    course = profile.get("class", "")
    stream = profile.get("academic_stream", "")
    grade_value = profile.get("grades_or_gpa", "").strip()

    try:
        gpa = float(grade_value)
    except ValueError:
        gpa = 0.0

        

    strong_subjects = [s.strip() for s in profile.get("strength_subjects", "").split(",") if s.strip()]
    weak_subjects = [s.strip() for s in profile.get("weak_subjects", "").split(",") if s.strip()]
    extracurriculars = [e.strip() for e in profile.get("extracurriculars", "").split(",") if e.strip()]
    skills = [s.strip() for s in profile.get("skills", "").split(",") if s.strip()]
    hobbies = [h.strip() for h in profile.get("hobbies", "").split(",") if h.strip()]

    # ---------- Strengths ----------
    if gpa >= 8.0:
        swot['strengths'].append(f"Good GPA ({gpa}/10) indicating strong academic performance")
    elif 6.5 <= gpa < 8.0:
        swot['strengths'].append(f"Moderate GPA ({gpa}/10), with scope to improve further")

    for subject in strong_subjects:
        swot['strengths'].append(f"Strong in subject: {subject}")

    # ---------- Weaknesses ----------
    if gpa < 6.0:
        swot['weaknesses'].append(f"Low GPA ({gpa}/10) which might affect competitive opportunities")

    # ---------- Threats ----------
    for subject in weak_subjects:
        swot['threats'].append(f"Weakness in subject: {subject}, which could impact related career options")

    # ---------- Opportunities ----------
    if course:
        swot['opportunities'].append(f"Can pursue advanced studies in the field of {course}")
    if stream:
        swot['opportunities'].append(f"Academic stream in {stream} offers various specialized career paths")

    for skill in skills:
        swot['opportunities'].append(f"Skill in {skill} is valuable in many industries")

    for activity in extracurriculars:
        swot['opportunities'].append(f"Involved in extracurricular activity: {activity}, which builds soft skills")

    return swot
