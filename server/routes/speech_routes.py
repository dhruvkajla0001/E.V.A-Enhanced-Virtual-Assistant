from flask import Blueprint, request, jsonify
from modules.speech.whisper_engine import transcribe_audio
from modules.speech.text_to_speech import speak_text

speech_bp = Blueprint('speech', __name__)

# === Speech-to-Text ===
@speech_bp.route('/stt', methods=['POST'])
def speech_to_text():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        audio_file = request.files['file']
        transcript = transcribe_audio(audio_file)
        return jsonify({"transcript": transcript})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Text-to-Speech ===
@speech_bp.route('/tts', methods=['POST'])
def text_to_speech():
    try:
        data = request.json
        text = data.get('text')
        if not text:
            return jsonify({"error": "Text is required"}), 400

        file_path = speak_text(text)
        return jsonify({"audio_path": file_path})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
