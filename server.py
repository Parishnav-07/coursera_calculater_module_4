"""Flask server for the Emotion Detector application."""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotion_detector', methods=['GET'])
def emotion_detection():
    """
    GET endpoint to analyze text for emotions.

    Query Parameters:
        text (str): The text to analyze.

    Returns:
        JSON response with emotion scores and dominant emotion,
        or a 400 error for blank/invalid input.
    """
    text_to_analyze = request.args.get('text', '')

    if not text_to_analyze or not text_to_analyze.strip():
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({'response': output, 'emotions': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
