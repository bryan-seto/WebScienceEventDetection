# PROJECT TITLE
# Web Science - Event Detection

# PREREQUISITES
# Download python from https://www.python.org/downloads/ (At least v3.6.2 or higher)
# Download MongoDB from https://www.mongodb.com/download-center (At least v4.0 or higher)
# Install Tweepy with "pip install tweepy"

# DEPLOYMENT
# 1) Create MongoDB with its name twitterdb
# 
# 1) Open command prompt (Hit on windows key and enter "CMD")
# 2) Navigate to the folder where the file is cd../2355373S_WEB_SCIENCE_EVENT_DETECTION
# 3) Enter "twitterRest.py"

# BUILT WITH
# 1) Tweepy - Communicate with Twitter platform
# 2) MongoDB - Database
# 3) Visual Studio Code - Code editor 


import json
import time
import tweepy
import datetime
from tweepy import Stream
from pymongo import MongoClient

# DATABASE CONNECTION
client = MongoClient()
db = client.twitter

MONGO_HOST= 'mongodb://localhost/twitterdb'  
client = MongoClient(MONGO_HOST)
db = client.twitterdb

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Call REST
WORDS = api.trends_place(23424948)
print(WORDS)
for x in WORDS:
    def RESTAPI(api):
        for item in tweepy.Cursor(api.search, q="WORDS").items():
            print(item.text)
            db.NEWtwitter_rest.insert(item._json)
            print(db.NEWtwitter_rest.count())
RESTAPI(api)