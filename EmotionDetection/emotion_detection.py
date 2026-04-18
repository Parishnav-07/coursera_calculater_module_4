"""Emotion detection module using Watson NLP library."""

import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the given text and detect emotions using Watson NLP.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion,
              or an error dict with status code 400 for blank/invalid input.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
        'NlpService/EmotionPredict'
    )
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    payload = {
        'raw_document': {
            'text': text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_data = response.json()

    emotions = (
        response_data
        .get('emotionPredictions', [{}])[0]
        .get('emotion', {})
    )

    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
    }

    emotion_scores['dominant_emotion'] = max(
        (k for k in emotion_scores),
        key=emotion_scores.get
    )

    return emotion_scores
