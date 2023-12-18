from bardapi import Bard
import os
import time

os.environ['_BARD_API_KEY']='dQgJH26N87QnmSuGbwg3v6_C534mm7o9lvY8IDzUA4a9ewNMK4KzX-P3ydJUdSYKROl-6A.'

# Function to predict sentiment
def predict_sentiment_bard(tweet):
    print("predict_sentiment_bard execution started")
    input_text = "Extract the sentiment as positive/negative or neutral from : "+tweet+" only give positive negative or neutral nothing else."
    result = Bard().get_answer(input_text)['content']
    print("predict_sentiment execution ended")
    print(result)
    return result

# Function to apply the classification for each tweet
def get_correct_topic_bard(tweet):
    input_text = "Extract topic and assign to ['service', 'delays', 'toilets', 'seats', 'wifi', 'tickets/seat_reservations', 'none', 'station', 'covid', 'doors', 'train_general', 'air conditioning', 'brakes', 'tables', 'plugs', 'noise', 'windows', 'hvac', 'announcements', 'vandalism', 'floor', 'roof', 'handrails'] the tweet is talking about from tweet: "+tweet+" and give the action the train department should perform to overcome the issue. Give only topic and specific action"
    output = Bard().get_answer(input_text)['content']
    input_text = "Give the result in the form Topic: , Action: from: "+output
    correct_topic = Bard().get_answer(input_text)['content']
    print(correct_topic)
    print("get_correct_topic_bard execution ended")
    return correct_topic
