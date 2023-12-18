# topic_predict_model.py

import pandas as pd
from transformers import pipeline
from getData import df

# Extract unique topics from the 'topic' column
potential_topics = df['topic'].unique().tolist()
print(potential_topics)

# Initialize the zero-shot-classification pipeline with the BART model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define a function to classify topics using zero-shot classification
def classify_topics(text, topics):
    result = classifier(text, candidate_labels=topics, hypothesis_template="This text is about which maintainance issue {}.")
    print(result)
    return result['labels'][0]  # Return the topic with the highest score

# Function to apply the classification for each tweet
def get_correct_topic(tweet):
    correct_topic = classify_topics(tweet, potential_topics)
    print(correct_topic)
    print("get_correct_topic execution ended")
    return correct_topic
