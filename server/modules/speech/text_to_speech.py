import pyttsx3
import uuid
import os

# === Initialize TTS engine ===
engine = pyttsx3.init()
engine.setProperty('rate', 170)        # Speed
engine.setProperty('volume', 1.0)      # Max volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (optional)

# === Directory to save audio files ===
AUDIO_DIR = "static/generated_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def speak_text(text):
    try:
        # Generate unique filename
        filename = f"{uuid.uuid4().hex}.mp3"
        file_path = os.path.join(AUDIO_DIR, filename)

        # Save spoken output to file
        engine.save_to_file(text, file_path)
        engine.runAndWait()

        return file_path

    except Exception as e:
        return f"Error in TTS: {str(e)}"
