from flask import Flask
from flask_cors import CORS

# === Import route blueprints ===
from routes.nlp_routes import nlp_bp
from routes.speech_routes import speech_bp
from routes.vision_routes import vision_bp
from routes.system_routes import system_bp

# === Initialize Flask App ===
app = Flask(__name__)

# === Enable CORS for frontend communication ===
CORS(app)

# === Register Blueprints (Modular Routing) ===
app.register_blueprint(nlp_bp, url_prefix='/api/nlp')
app.register_blueprint(speech_bp, url_prefix='/api/speech')
app.register_blueprint(vision_bp, url_prefix='/api/vision')
app.register_blueprint(system_bp, url_prefix='/api/system')

# === Root Health Check ===
@app.route('/')
def home():
    return {"status": "E.V.A backend is running 🧠"}

# === Run Server ===
if __name__ == '__main__':
    app.run(debug=True, port=5000)
