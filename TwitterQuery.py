#script for querying data using Twitter API- Standard Search
import twitter
import json
import csv

#set the keys to access twitter data
api = twitter.Api(consumer_key = "03THogY9wE1YUDTJHIFDwtwyH", \
	consumer_secret = "WPGTswYPmQCbWHL6lZrMad3Tc6eZunIYn5lEi59ymwFex6Q53b",\
	access_token_key = "1217097382300614657-IP2T38cKThKvLdKBGN0pUF9twhdMs6", \
	access_token_secret = "a4akT9nmIasnDFZSwv43DzXe2oG66YI0RVJNsB1gEpMG0")

results = api.GetSearch(raw_query = "lang=en&q=lang%3Aen%20&until%3A2020-01-10&src=typed_query", geocode=[37.781157, -122.398720, "45mi"])
for result in results:
	print(result.created_at)
	print(result.coordinates)
	print()
	


