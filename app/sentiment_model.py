import pickle
import tensorflow as tf
import pkg_resources

from dataclasses import dataclass
from tensorflow.keras.preprocessing.sequence import pad_sequences
from symspellpy.symspellpy import SymSpell

MODEL_PATH = 'model/sentiment_model.keras'
TOKENIZER_PATH = 'model/tokenizer.pickle'
THRESHOLD = 0.55

# Initialize SymSpell
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
bigram_path = pkg_resources.resource_filename("symspellpy", "frequency_bigramdictionary_en_243_342.txt")

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

@dataclass
class SentimentPredictionResponse:
    POSITIVE = "Positive"
    NEGATIVE = "Negative"

    sentiment: str
    confidence: float

class CustomSentimentModel:

    def __init__(self):
        # Load the trained model
        self.model = tf.keras.models.load_model(MODEL_PATH)

        # Tokenizer settings (should match the training settings)
        # Load the tokenizer
        with open(TOKENIZER_PATH, 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    def predict(self, text: str) -> SentimentPredictionResponse:

        corrected_text = sym_spell.lookup_compound(text, max_edit_distance=2)

        if corrected_text:
            corrected_text = corrected_text[0].term
        else:
            corrected_text = text

        # Tokenize and pad the input text
        sequences = self.tokenizer.texts_to_sequences([corrected_text])
        padded_sequences = pad_sequences(sequences, maxlen=100)

        # Predict sentiment
        prediction = self.model.predict(padded_sequences)

        is_negative = False if prediction[0][0] <= THRESHOLD else True
        sentiment = SentimentPredictionResponse.POSITIVE if not is_negative else SentimentPredictionResponse.NEGATIVE

        prediction = float(prediction[0][0])
        confidence = 1 - prediction if not is_negative else prediction

        return SentimentPredictionResponse(sentiment=sentiment, confidence=confidence)