import openai
from api_key import api_key

openai.api_key = api_key 

def get_combined_analysis_and_token_usage(tweet):
    prompt = (
        f"Analyze this tweet: '{tweet}'. Classify the sentiment as either positive or negative. "
        "Identify the main topic from these options: air conditioning, announcements, brakes, COVID, delays, doors, floor, handrails, hvac, "
        "noise, plugs, roof, seats, service, station, tables, tickets/seat reservations, toilets, train general, vandalism, wifi, windows. "
        "Based on the sentiment and topic, suggest an appropriate and specific action for train maintainance team in maximum 5 words."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI trained to analyze social media content. Provide concise answers for the given tasks."},
            {"role": "user", "content": prompt}
        ]
    )
    result = response.choices[0].message['content']
    print(result)
    # token_usage = response.usage
    return result #, token_usage


# combined_prompt = 'I love this train conductor(?), he''s apologised for a non-working toilet and told us where the next working toilets are. He also said the next station may be busy, and to be warned, but also might not. "it was heaving earlier today"#thameslink'
# combined_analysis= get_combined_analysis_and_token_usage(combined_prompt)

# Extract sentiment, topic, and action from the lines
def get_sentiment(combined_result):
    lines = combined_result.split('\n')
    sentiment = lines[0].split(': ')[1]
    return sentiment

def get_topic(combined_result):
    lines = combined_result.split('\n')
    topic = lines[1].split(': ')[1]
    return topic

def get_Action(combined_result):
    lines = combined_result.split('\n')
    action = lines[2].split(': ')[1]
    return action

# print("Sentiment:", get_sentiment(combined_analysis))
# print("Topic:", get_topic(combined_analysis))
# print("Action:", get_Action(combined_analysis))
