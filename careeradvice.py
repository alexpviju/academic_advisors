import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

# Zephyr is a chat-tuned LLM with great advice quality
client = InferenceClient(
    model="HuggingFaceH4/zephyr-7b-beta",
    token=HF_API_KEY
)

def generate_advice(swot: dict) -> str:
    prompt = f"""
You are an experienced academic and career counselor.
Provide clear, personalized advice for the student based on this SWOT analysis.

Strengths:
{', '.join(swot['strengths']) or 'None'}

Weaknesses:
{', '.join(swot['weaknesses']) or 'None'}

Opportunities:
{', '.join(swot['opportunities']) or 'None'}

Threats:
{', '.join(swot['threats']) or 'None'}

Give helpful, motivating, and realistic advice in 5–7 sentences.
"""

    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=350,
            temperature=0.7,
            do_sample=True,
            stop_sequences=["\n\n"]
        )
        return response.strip()

    except Exception as e:
        print("Error generating advice:", e)
        return "An error occurred while generating your advice. Please try again later."
