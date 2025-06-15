from flask import Flask, request, render_template
from swot_generator import perform_swot_analysis
from careeradvice import generate_advice
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect input data from the form
    profile = {
        "name": request.form.get("name"),
        "age": request.form.get("age"),
        "class": request.form.get("class"),
        "academic_stream": request.form.get("academic_stream"),
        "grade_type": request.form.get("grade_type"),
        "grades_or_gpa": request.form.get("grades_or_gpa"),
        "strength_subjects": request.form.get("strength_subjects"),
        "weak_subjects": request.form.get("weak_subjects"),
        "extracurriculars": request.form.get("extracurriculars"),
        "skills": request.form.get("skills"),
        "hobbies": request.form.get("hobbies")
    }

    # Perform SWOT analysis
    swot_result = perform_swot_analysis(profile)

    # Generate career advice using OpenAI
    advice = generate_advice(swot_result)

    return render_template(
        "result.html",
        name=profile["name"],
        swot=swot_result,
        advice=advice
    )

if __name__ == "__main__":
    app.run(debug=True)
