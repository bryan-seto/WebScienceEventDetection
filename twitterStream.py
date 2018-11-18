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
# 3) Enter "twitterStream.py"

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

# STREAMING API
class StreamListener(tweepy.StreamListener):    

    def on_connect(self):
        # Connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # If error occurs, display the error code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        # Connects to MongoDB and stores the tweet
        try:
            # Decode JSON from Twitter
            datajson = json.loads(data)
            
            # Insert data to MongoDB > Collection > twitter_stream 
            # If twitter_stream doesn't exist, will be created.
            db.NEWtwitter_stream.insert(datajson)

        except Exception as e:
           print(e)

# Call STREAM
language = ['en']
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
streamer.filter(track=['#stanlee'],languages=language, locations =[103.6182, 1.1158, 104.4085, 1.4706], async=True)  

