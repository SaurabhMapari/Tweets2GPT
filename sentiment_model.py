# sentiment_model.py

from transformers import pipeline

# Load the model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define the sentiment classes
classes = ["positive", "negative", "neutral"]

# Function to predict sentiment
def predict_sentiment(tweet):
    print("predict_sentiment execution started")
    result = classifier(tweet, classes)
    print("predict_sentiment execution ended")
    print(result)
    return result['labels'][0]
