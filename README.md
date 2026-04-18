# Emotion Detector - AI-Based Web Application

An emotion detection web application built with Python, Flask, and Watson NLP for the Coursera Module 4 assignment. This project demonstrates building, packaging, testing, and deploying an AI-based web application.

## Description

The Emotion Detector analyzes text input and identifies five emotions: **joy**, **sadness**, **fear**, **disgust**, and **anger**. It returns the score for each emotion and identifies the dominant emotion.

## Project Structure

```
coursera_calculater_module_4/
├── README.md
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── server.py
├── test_emotion_detection.py
└── requirements.txt
```

## Features

- Detects 5 emotions: joy, sadness, fear, disgust, anger
- Returns emotion scores and dominant emotion
- Error handling with HTTP 400 for blank/invalid input
- Flask REST API with GET endpoint
- 10 comprehensive unit tests (all passing)
- Static code analysis score: 10.00/10 (pylint)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run the Flask server

```bash
python server.py
```

### Call the API

```bash
curl "http://localhost:5000/emotion_detector?text=I am so happy today!"
```

### Run unit tests

```bash
python -m pytest test_emotion_detection.py -v
```

### Run static code analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py test_emotion_detection.py
```

## API Endpoint

**GET** `/emotion_detector?text=<your_text>`

**Success Response (200):**
```json
{
  "response": "For the given statement, the system response is 'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.9 and 'sadness': 0.1. The dominant emotion is joy.",
  "emotions": {
    "anger": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "joy": 0.9,
    "sadness": 0.1,
    "dominant_emotion": "joy"
  }
}
```

**Error Response (400):**
```json
{
  "error": "Invalid text! Please try again!"
}
```

## License

This project is licensed under the Apache 2.0 License.