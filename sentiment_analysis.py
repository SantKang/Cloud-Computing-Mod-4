from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app and sentiment analysis model
app = Flask(__name__)
sentiment_model = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        # Perform sentiment analysis
        result = sentiment_model(text)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)  # OpenShift uses port 8080
