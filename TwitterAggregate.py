#obtain latest twitter data and process it for desired data
import pandas as pd
import numpy as np
from datetime import datetime

#read file 
tweets = pd.read_csv("/home/colinphillips17/Desktop/TAVtech/tweets_w_dates2.csv")
tweets = tweets[["Tweets","Dates"]]
df = pd.DataFrame({'Latitude': np.random.randn(1000), \
                   'Longitude': np.random.randn(1000)})

#generate appropriate dates and random geographic data
tweets["Dates"] = tweets["Dates"].str[0:-9]
tweets["Dates"] = pd.to_datetime(tweets['Dates'])
df["Latitude"] = df["Latitude"]+4.0383
df["Longitude"]= df["Longitude"]+21.7587

tweets["Longitude"] = df["Longitude"]
tweets["Latitude"] = df["Latitude"]

#obtain csv
tweets.to_csv("lastSevenDays_data.csv")