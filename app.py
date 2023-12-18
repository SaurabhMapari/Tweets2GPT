# app.py
import webbrowser
from threading import Timer
from flask import Flask, render_template, request, jsonify
# from sentiment_model import predict_sentiment
# from topic_predict_model import get_correct_topic
# from bard import get_correct_topic_bard, predict_sentiment_bard
from datetime import datetime, timedelta
from chatgpt import get_combined_analysis_and_token_usage,get_Action,get_sentiment,get_topic
import mysql.connector

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tweet2gpt"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_tweet', methods=['POST'])
def analyze_tweet():
    data = request.json  # Get JSON data from the request
    tweet = data['tweet']
    # sentiment = predict_sentiment(tweet)
    # topic = get_correct_topic(tweet)
    # action = 'No Action'
    # topic = 'Air Conditioning'
    # sentiment = predict_sentiment_bard(tweet)
    # topic = get_correct_topic_bard(tweet)
    # print("Topic:", "HVAC")
    # print("Sentiment:", "Negative")


    ###################################################################################################### ChatGPT ##########################################################################################################
    combined_result = get_combined_analysis_and_token_usage(tweet)
    # combined_result = """Sentiment: Positive
    #                     Main Topic: Toilets
    #                     Action: Improve toilet maintenance and cleanliness."""
    sentiment = get_sentiment(combined_result)
    topic = get_topic(combined_result)
    action = get_Action(combined_result)
    ###################################################################################################### ChatGPT ##########################################################################################################

    ###########################################################################################################
    # sentiment = 'Positive'
    # topic = 'Toilets'
    # action = 'Improve toilet maintenance and cleanliness.'

    ################################################################################################################
     # Current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insert data into database
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    insert_query = """
        INSERT INTO tweets (text, topic, sentiment, source_created_at, source) 
        VALUES (%s, %s, %s, %s, 'local')
    """
    cursor.execute(insert_query, (tweet, topic, sentiment, current_time))
    db_connection.commit()
    cursor.close()
    db_connection.close()

    return jsonify(sentiment=sentiment, topic=topic, action = action)

# import os

# webbrowser.open_new('http://127.0.0.1:5000/')

# if __name__ == '__main__':
#   app.run(debug=False)