"""Wrapper module for analyzing sentiment within text"""
import os
from typing import Tuple
from google.cloud import language_v1

# Setup OCP IAM environmental var
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join('iam', 'timely-gcp-iam.json')

def evaluate_sentiment(text_to_analyze: str) -> Tuple[float, float]:
    """Wrapper for calling Google Cloud Platform Language Service Client
 
    Arguments:
        text_to_analyze: Text to be run through sentiment analysis

    Returns:
        sentiment_score: floating point value (between -1 and 1)
            representing sentiment as a percentage
        sentiment_magnitude: floating point value (no max)
            representing how emotional the content of the text is
    """
    nlp_client = language_v1.LanguageServiceClient()
    document = {"content" : text_to_analyze,
                "type": language_v1.Document.Type.PLAIN_TEXT,
                "language": "en"}

    document = language_v1.Document(
        content=text_to_analyze, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    # Call GCP
    sentiment = nlp_client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    # Return sentiment score and magnitude
    return sentiment.score, sentiment.magnitude
