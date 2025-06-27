from flask import Blueprint, request, jsonify
from modules.automation.system_commands import execute_command

system_bp = Blueprint('system', __name__)

# === Run System Command (open app, browser, play song) ===
@system_bp.route('/run', methods=['POST'])
def run_command():
    try:
        data = request.json
        command = data.get('command')
        if not command:
            return jsonify({"error": "Command is required"}), 400

        result = execute_command(command)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
