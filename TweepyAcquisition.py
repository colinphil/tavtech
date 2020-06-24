#using tweepy to filter twitter data and create csv
import tweepy
from tweepy import OAuthHandler
import json
import csv
import pandas as pd

CONSUMER_KEY = "03THogY9wE1YUDTJHIFDwtwyH"
CONSUMER_SECRET = "WPGTswYPmQCbWHL6lZrMad3Tc6eZunIYn5lEi59ymwFex6Q53b"
OAUTH_TOKEN = "1217097382300614657-IP2T38cKThKvLdKBGN0pUF9twhdMs6"
OAUTH_TOKEN_SECRET = "a4akT9nmIasnDFZSwv43DzXe2oG66YI0RVJNsB1gEpMG0"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True)

search_words = "sars" + " -filter:retweets"

tweetsList = []
datesList = []
tweets = tweepy.Cursor(api.search,q=search_words).items(1000)
for tweet in tweets:
	tweetsList.append(tweet.text)
	datesList.append(tweet.created_at)

tweetsFrame = pd.DataFrame({"Tweets":tweetsList,"Dates": datesList})
print(len(tweetsList))
tweetsFrame.to_csv("sars_w_dates.csv")

