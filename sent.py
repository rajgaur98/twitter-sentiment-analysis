import tweepy
from textblob import TextBlob
import pandas as pd


consumer_key = '1mT9owMybiFFAyxwLUBGAjH7m'
consumer_secret = 'gXfHUb0wYKvKQqAChvgYTltqH78fZCmOVgtXu83ruqiFQfKOUl'

access_token = '1178665560948658176-NA2107N05T2DecC1feuPS6MIdfWPHe'
access_token_secret = 'ZxEspFNgHQY119NTsErp0mT74qUCPpIDbVIHOFPtD0fDS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('India')

tweet_data = []
sentiment = []

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    tweet_data.append(tweet.text)
    if(analysis.sentiment.polarity > 0):
        sentiment.append('happy')
    elif(analysis.sentiment.polarity == 0):
        sentiment.append('neutral')
    elif(-0.25 < analysis.sentiment.polarity < 0):
        sentiment.append('unhappy')
    else:
        sentiment.append('sad')

dict = {'sentence': tweet_data, 'sentiment': sentiment}

df = pd.DataFrame(dict)

df.to_csv('results.csv')

