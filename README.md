# Sentiment Analysis Flask App

This is a Flask web application that performs sentiment analysis on user-provided text using a pre-trained TensorFlow model.

## Features

- **Web Interface**: Users can input text and get sentiment analysis results.
- **API Endpoint**: Provides a `/predict` endpoint to get sentiment predictions via POST requests.

## Requirements

- Python 3.6+
- Flask
- TensorFlow
- Numpy
- Pickle

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages**:
    ```bash
    pip install pipenv
    pipenv shell
    pipenv install
    ```

## Usage

1. **Run the Flask app**:
    ```bash
    python app/app.py
    ```

2. **Access the web interface**:
    Open your web browser and go to `http://127.0.0.1:5001/`.

3. **Use the API endpoint**:
    - Send a POST request to `http://127.0.0.1:5001/predict` with a JSON body containing the text to analyze.
    ```bash
    curl -X POST http://127.0.0.1:5001/predict -H "Content-Type: application/json" -d '{"text": "Your text here"}'
    ```

## File Structure
