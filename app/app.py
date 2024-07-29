from flask import Flask, request, jsonify, render_template

import app.sentiment_model as model

app = Flask(__name__)

custom_sentiment_model = model.CustomSentimentModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    prediction = custom_sentiment_model.predict(text)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)