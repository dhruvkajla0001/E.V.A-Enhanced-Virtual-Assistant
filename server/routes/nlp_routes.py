from flask import Blueprint, request, jsonify
from modules.nlp.brain import process_text

nlp_bp = Blueprint('nlp', __name__)

@nlp_bp.route('/ask', methods=['POST'])
def ask_eva():
    try:
        data = request.json
        user_input = data.get('question')

        if not user_input:
            return jsonify({"error": "Missing input"}), 400

        response = process_text(user_input)
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
