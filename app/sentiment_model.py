import pickle
import tensorflow as tf

from dataclasses import dataclass
from tensorflow.keras.preprocessing.sequence import pad_sequences

MODEL_PATH = 'model/sentiment_model.keras'
TOKENIZER_PATH = 'model/tokenizer.pickle'
THRESHOLD = 0.5

@dataclass
class SentimentPrediction:
    sentiment: str
    confidence_to_be_negative: float

class SentimentModel:

    def __init__(self):
        # Load the trained model
        self.model = tf.keras.models.load_model(MODEL_PATH)

        # Tokenizer settings (should match the training settings)
        # Load the tokenizer
        with open(TOKENIZER_PATH, 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def predict(self, text) -> SentimentPrediction:

        # Tokenize and pad the input text
        sequences = self.tokenizer.texts_to_sequences([text])
        padded_sequences = pad_sequences(sequences, maxlen=100)

        # Predict sentiment
        prediction = self.model.predict(padded_sequences)
        sentiment = 'positive' if prediction[0][0] < THRESHOLD else 'negative'

        return SentimentPrediction(sentiment=sentiment, confidence_to_be_negative=float(prediction[0][0]))