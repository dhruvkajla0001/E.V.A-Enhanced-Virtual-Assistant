import whisper
import tempfile

# === Load Whisper Model (base/medium/small/tiny/large) ===
model = whisper.load_model("base")  # Use "tiny" for faster results

# === Function to transcribe audio ===
def transcribe_audio(audio_file):
    try:
        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            audio_file.save(temp_audio.name)
            result = model.transcribe(temp_audio.name)
            return result["text"]

    except Exception as e:
        return f"Whisper STT Error: {str(e)}"
