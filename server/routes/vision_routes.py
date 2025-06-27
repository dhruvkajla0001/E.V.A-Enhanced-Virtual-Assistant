from flask import Blueprint, request, jsonify
from modules.vision.face_recognition import recognize_face
from modules.vision.gesture_control import detect_gesture
from modules.vision.object_detection import detect_objects

vision_bp = Blueprint('vision', __name__)

# === Face Recognition ===
@vision_bp.route('/face', methods=['POST'])
def face_recognition():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['image']
        result = recognize_face(image_file)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Gesture Recognition ===
@vision_bp.route('/gesture', methods=['POST'])
def gesture_recognition():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['image']
        result = detect_gesture(image_file)
        return jsonify({"gesture": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === Object Detection (YOLO or OpenCV) ===
@vision_bp.route('/detect', methods=['POST'])
def object_detection():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['image']
        result = detect_objects(image_file)
        return jsonify({"objects": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
