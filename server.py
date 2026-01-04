from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotion_detector_route():
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze") 
    else:
        data = request.get_json(silent=True) or {}
        text_to_analyze = data.get('text') or data.get('statement')
        
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text_to_analyze)
    
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return response_text, 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
