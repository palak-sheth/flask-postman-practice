from flask import Flask, request, jsonify, g
import uuid
import logging
import json
import os
from dotenv import load_dotenv


# -----------------------
# Load .env
# -----------------------
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN", "SECRET123")  # fallback if missing

app = Flask(__name__)

# -----------------------
# Logging Configuration
# -----------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)
logger = logging.getLogger(__name__)

# -----------------------
# Request ID Middleware
# -----------------------
@app.before_request
def assign_request_id():
    g.request_id = str(uuid.uuid4())

# -----------------------
# Auth Middleware (only for /chat, /summarize, /extract)
# -----------------------
@app.before_request
def check_token():
    protected_paths = ['/chat', '/summarize', '/extract']

    if request.path in protected_paths:
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if token != API_TOKEN:
            return jsonify({"error": "Unauthorized"}), 401


# -----------------------
# Error Handler (JSON output)
# -----------------------
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(json.dumps({
        "event": "error",
        "request_id": g.get("request_id"),
        "error": str(e)
    }))
    return jsonify({"error": "Internal Server Error"}), 500


# --- /chat endpoint ---
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    logger.info(json.dumps({
        "event": "chat_request_received",
        "request_id": g.request_id,
        "payload": data
    }))

    message = data.get('message', '')
    response = {"reply": f"You said: {message}"}

    logger.info(json.dumps({
        "event": "chat_response_sent",
        "request_id": g.request_id,
        "response": response
    }))

    return jsonify(response)


# --- /summarize endpoint ---
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    logger.info(json.dumps({
        "event": "summarize_request_received",
        "request_id": g.request_id,
        "payload": data
    }))

    text = data.get('text', '')
    summary = text[:50] + "..." if len(text) > 50 else text
    response = {"summary": summary}

    logger.info(json.dumps({
        "event": "summarize_response_sent",
        "request_id": g.request_id,
        "response": response
    }))

    return jsonify(response)


# --- /extract endpoint ---
@app.route('/extract', methods=['POST'])
def extract():
    data = request.get_json()
    logger.info(json.dumps({
        "event": "extract_request_received",
        "request_id": g.request_id,
        "payload": data
    }))

    text = data.get('text', '')
    keywords = [w for w in text.split() if len(w) > 5]
    response = {"keywords": keywords}

    logger.info(json.dumps({
        "event": "extract_response_sent",
        "request_id": g.request_id,
        "response": response
    }))

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
