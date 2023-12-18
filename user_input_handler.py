# user_input_handler.py

from sentiment_model import predict_sentiment

# This line prompts the user to input something and stores it in a variable named 'user_input'
user_input = input("Please enter tweet: ")

# Get sentiment
sentiment = predict_sentiment(user_input)

# Print the sentiment
print("Sentiment:", sentiment)
