import pickle
import numpy as np
import tensorflow as tf

from flask import Flask, request, jsonify, render_template
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the trained model
model = tf.keras.models.load_model('model/sentiment_model.h5')

# Initialize Flask app
app = Flask(__name__)

# Tokenizer settings (should match the training settings)
# Load the tokenizer
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    
    # Tokenize and pad the input text
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=100)

    print("sequence, text, padded", sequences, text, padded_sequences)
    
    # Predict sentiment
    prediction = model.predict(padded_sequences)
    sentiment = 'positive' if prediction[0][0] < 0.5 else 'negative'
    
    return jsonify({'sentiment': sentiment, 'confidence_to_be_negative': float(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)