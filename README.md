
# 🎓 SWOT-Based Career Advice Generator

This project is a web application that performs a **SWOT analysis** (Strengths, Weaknesses, Opportunities, Threats) based on a student's academic profile and generates personalized **career advice** using a Hugging Face language model.

## 📌 Features

- Collects academic, extracurricular, and personal skill data via a web form
- Generates a detailed SWOT analysis
- Provides customized career advice using an LLM from Hugging Face
- Built with **Flask** (Python backend) and **HTML** (frontend)
- API integration with **Hugging Face Transformers**

---

## 🛠️ Technologies Used

- Python 3.12+
- Flask
- Hugging Face Transformers
- HTML/CSS
- dotenv
- TensorFlow (optional if using compatible model)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/swot-career-advice.git
cd swot-career-advice
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your Hugging Face API key:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here
```

### 5. Run the Application

```bash
python app.py
```

Access the web app at: `http://127.0.0.1:5000`

---

## 🧠 File Structure

```
.
├── app.py                 # Flask server
├── careeradvice.py        # Hugging Face API integration
├── swot_generator.py      # SWOT logic processor
├── templates/
│   ├── index.html         # User input form
│   └── result.html        # Output SWOT + advice
├── .env                   # API Key (not to be shared)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📄 Example Inputs

User provides:
- Name, Age, Class
- Academic stream and GPA
- Strong/weak subjects
- Skills, hobbies, extracurriculars

Output:
- SWOT analysis
- A short paragraph of personalized career advice

---

## ✅ To Do (Suggestions)

- Add session tracking to handle multiple users
- Save SWOT and advice to a database or CSV
- Add model selection dropdown (OpenAI / Hugging Face)
- Deploy to a cloud platform (e.g., Heroku, Render)

---

## 📬 Contact

For questions or suggestions, feel free to reach out:
**Alex P V **  
📧 alexpviju26@gmail.com

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
