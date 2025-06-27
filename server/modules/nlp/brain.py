import os
import google.generativeai as genai
from dotenv import load_dotenv

# === Load Gemini API Key ===
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# === Configure Gemini ===
genai.configure(api_key=GEMINI_API_KEY)

# === Create Model Instance (Gemini Flash 2.0) ===
model = genai.GenerativeModel("models/gemini-2.0-flash")

# === Chat session for memory (optional)
chat = model.start_chat(history=[
    {
        "role": "system",
        "parts": [
            "You are E.V.A — a confident, intelligent, and futuristic personal assistant. "
            "You respond like a real AI from sci-fi. Be helpful, concise, and powerful. "
            "Avoid saying you're a language model. Your tone is smart and engaging."
        ]
    }
])

# === Process user input via Gemini ===
def process_text(user_input):
    try:
        response = chat.send_message(user_input)
        return response.text.strip()

    except Exception as e:
        return f"Oops, EVA encountered an error: {str(e)}"
