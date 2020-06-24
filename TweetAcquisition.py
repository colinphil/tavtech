#script for acquiring tweets using tweet id

#import appropriate modules
import twitter
import json
import csv

#set the keys for accessing twitter
CONSUMER_KEY = "03THogY9wE1YUDTJHIFDwtwyH"
CONSUMER_SECRET = "WPGTswYPmQCbWHL6lZrMad3Tc6eZunIYn5lEi59ymwFex6Q53b"
OAUTH_TOKEN = "1217097382300614657-IP2T38cKThKvLdKBGN0pUF9twhdMs6"
OAUTH_TOKEN_SECRET = "a4akT9nmIasnDFZSwv43DzXe2oG66YI0RVJNsB1gEpMG0"

#access tweet dat
tweet_data = open("/home/colinphillips17/Downloads/2014-ebola.ids","r")
id_of_tweet = tweet_data.readline().strip()

#create tweet object
api = twitter.Api(consumer_key = CONSUMER_KEY, \
	consumer_secret = CONSUMER_SECRET,\
	access_token_key = OAUTH_TOKEN, \
	access_token_secret = OAUTH_TOKEN_SECRET)

#iterate through to access tweets using id
#terminates after the 22nd iteration 
count = 0
while id_of_tweet != "":
	count+=1
	print(count)
	tweet = api.GetStatus(status_id = id_of_tweet)
	print(tweet.created_at)
	print(tweet.text,"\n")
	id_of_tweet = tweet_data.readline().strip()
