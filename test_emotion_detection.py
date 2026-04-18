"""Unit tests for the EmotionDetection module."""

import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def _mock_response(self, emotions):
        """Helper to create a mock API response."""
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            'emotionPredictions': [{'emotion': emotions}]
        }
        return mock_resp

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_detection(self, mock_post):
        """Test that joy is detected as dominant emotion."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.9, 'sadness': 0.1}
        )
        result = emotion_detector('I am so happy today!')
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_detection(self, mock_post):
        """Test that sadness is detected as dominant emotion."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.1, 'sadness': 0.9}
        )
        result = emotion_detector('I feel very sad and lonely.')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_detection(self, mock_post):
        """Test that fear is detected as dominant emotion."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.0, 'disgust': 0.0, 'fear': 0.9, 'joy': 0.0, 'sadness': 0.1}
        )
        result = emotion_detector('I am terrified of the dark.')
        self.assertEqual(result['dominant_emotion'], 'fear')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_detection(self, mock_post):
        """Test that disgust is detected as dominant emotion."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.0, 'disgust': 0.9, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.1}
        )
        result = emotion_detector('This is absolutely disgusting.')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_detection(self, mock_post):
        """Test that anger is detected as dominant emotion."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.9, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.1}
        )
        result = emotion_detector('I am extremely angry right now!')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_blank_input_returns_none(self):
        """Test that blank input returns None values."""
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])

    def test_whitespace_input_returns_none(self):
        """Test that whitespace-only input returns None values."""
        result = emotion_detector('   ')
        self.assertIsNone(result['dominant_emotion'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_result_contains_all_emotions(self, mock_post):
        """Test that result dict contains all five emotion keys."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.1, 'disgust': 0.1, 'fear': 0.1, 'joy': 0.6, 'sadness': 0.1}
        )
        result = emotion_detector('I feel okay.')
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(emotion, result)

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_result_is_dict(self, mock_post):
        """Test that the result is a dictionary."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.1, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.8, 'sadness': 0.1}
        )
        result = emotion_detector('Hello world!')
        self.assertIsInstance(result, dict)

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_dominant_emotion_is_string(self, mock_post):
        """Test that the dominant_emotion value is a string."""
        mock_post.return_value = self._mock_response(
            {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.8, 'sadness': 0.2}
        )
        result = emotion_detector('Life is beautiful!')
        self.assertIsInstance(result['dominant_emotion'], str)


if __name__ == '__main__':
    unittest.main()
