# PROJECT TITLE
# Web Science - Event Detection
# 2355373S - Bryan Se To Zhan Yuan

# PREREQUISITES
# Download python from https://www.python.org/downloads/ (At least v3.6.2 or higher)
# Download MongoDB from https://www.mongodb.com/download-center (At least v4.0 or higher)
# Install praw with "pip install praw"

# DEPLOYMENT
# 1) Create MongoDB with its name redditdb
# 
# 1) Open command prompt (Hit on windows key and enter "CMD")
# 2) Navigate to the folder where the file is cd../2355373S_WEB_SCIENCE_EVENT_DETECTION
# 3) Enter "redditRest.py"

# BUILT WITH
# 1) PRAW - Communicate with Reddit platform
# 2) MongoDB - Database
# 3) Visual Studio Code - Code editor 

import praw
import json
import time
import tweepy
import datetime
from tweepy import Stream
from pymongo import MongoClient

# DATABASE CONNECTION
client = MongoClient()
db = client.reddit

MONGO_HOST= 'mongodb://localhost/redditdb'  
client = MongoClient(MONGO_HOST)
db = client.redditdb

# Get PRAW which dynamically handles the rate limiting (30 requests per minute)
reddit = praw.Reddit(client_id='',
                     client_secret='', password='',
                     user_agent='', username='')

# Search for all sub reddits with no limit so that the API can keep running
subreddit = reddit.subreddit('all') 
# Seacrch for the hottest topics
hot_subReddit = subreddit.hot(limit=None)

# Parse the object to JSON
for subRed in hot_subReddit:
    data = {}
    data['id'] = subRed.id
    data['author'] = subRed.author
    data['created_utc'] = subRed.created_utc
    data['distinguished'] = subRed.distinguished
    data['score'] = subRed.score
    data['title'] = subRed.title
    data['score'] = subRed.score
    data['num_comments'] = subRed.num_comments
    data['selftext'] = subRed.selftext
    data['upvote_ratio'] = subRed.upvote_ratio

    # Since author is an instance, have to manually sort the data columns 
    aut = {}
    aut['name'] = subRed.author.name
    aut['comment_karma'] = subRed.author.comment_karma
    aut['created_utc'] = subRed.author.created_utc
    aut['id'] = subRed.author.id
    aut['name'] = subRed.author.name
    data['author'] = aut

    print(data)
    db.reddit.insert(data)

#Analytics: Use The Most Frequently Used Words In Reddit Submission Titles From 2016 To 2018 and compare which words give how high of a score 
# X-axis: Different kind of words: time, people, irl, day, til, found, love, life, happy
# Y-axis: 0 to 10000, 10000 to 20000, 20000 >