from flask import Flask, request, jsonify
from services.strength_analyzer import analyze_strength
from services.breach_checker import check_breach
from services.pattern_detector import detect_patterns

app = Flask(__name__)

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