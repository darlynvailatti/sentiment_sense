import pytest
from app.sentiment_model import CustomSentimentModel, SentimentPredictionResponse


class TestSentimentModel:

    @pytest.fixture
    def sentiment_model(self):
        return CustomSentimentModel()

    def test_model_initialization(self, sentiment_model):
        assert sentiment_model.model is not None, "Model should be loaded"
        assert sentiment_model.tokenizer is not None, "Tokenizer should be loaded"

    def test_prediction(self, sentiment_model):
        sample_text = "I love this product!"
        response = sentiment_model.predict(sample_text)

        assert isinstance(
            response, SentimentPredictionResponse
        ), "Response should be of type SentimentPredictionResponse"
        assert response.sentiment in [
            SentimentPredictionResponse.POSITIVE,
            SentimentPredictionResponse.NEGATIVE,
        ], "Sentiment should be either Positive or Negative"
        assert 0.0 <= response.confidence <= 1.0, "Confidence should be between 0 and 1"

    @pytest.mark.parametrize(
        "text, expected_sentiment",
        [
            ("I love this product!", SentimentPredictionResponse.POSITIVE),
            ("I hate this product!", SentimentPredictionResponse.NEGATIVE),
        ],
    )
    def test_predictions(self, text, expected_sentiment, sentiment_model):
        response = sentiment_model.predict(text)
        assert response.sentiment == expected_sentiment, "Sentiment should match"
        assert 0.0 <= response.confidence <= 1.0, "Confidence should be between 0 and 1"
