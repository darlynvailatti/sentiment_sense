from flask import Flask, request, jsonify, render_template

import sentiment_model as model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    prediction = model.SentimentModel().predict(text)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)