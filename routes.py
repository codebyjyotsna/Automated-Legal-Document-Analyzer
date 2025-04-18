from flask import Blueprint, request, jsonify, render_template
from app.utils.file_handler import handle_uploaded_file
from app.utils.nlp_processor import simplify_text, summarize_text
from app.utils.risk_analyzer import analyze_risks

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template("index.html")

@routes.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        text = handle_uploaded_file(file)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route('/analyze', methods=['POST'])
def analyze_document():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    simplified_text = simplify_text(text)
    risks = analyze_risks(text)
    summary = summarize_text(text)

    return jsonify({
        "simplified_text": simplified_text,
        "risks": risks,
        "summary": summary
    })
