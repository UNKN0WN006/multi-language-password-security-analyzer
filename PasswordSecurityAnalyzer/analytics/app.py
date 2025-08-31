from flask import Flask, request, jsonify
from services.strength_analyzer import analyze_strength
from services.breach_checker import check_breach
from services.pattern_detector import detect_patterns


app = Flask(__name__)

# Root route for health check
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Password Security Analyzer API is running. Use POST /api/analyze."})

# Test route for demonstration
@app.route('/test', methods=['GET'])
def test():
    sample_password = "YourTestPassword123!"
    strength_analysis = analyze_strength(sample_password)
    breach_status = check_breach(sample_password)
    patterns = detect_patterns(sample_password)
    response = {
        'strength': strength_analysis,
        'breach': breach_status,
        'patterns': patterns
    }
    return jsonify(response)

@app.route('/api/analyze', methods=['POST'])
def analyze_password():
    data = request.json
    password = data.get('password', '')

    strength_analysis = analyze_strength(password)
    breach_status = check_breach(password)
    patterns = detect_patterns(password)

    response = {
        'strength': strength_analysis,
        'breach': breach_status,
        'patterns': patterns
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)