import re
import pandas as pd

def most_retweeted(tweets):
    tweets = tweets.sort_values(by="retweetCount", ascending=False).head(10)
    return tweets[['content', 'retweetCount']]

def most_active_users(tweets, users):
    tweets.groupby(['userId']).size()
    return

def most_active_days(tweets):
    pass

def most_frecuent_hashtags(tweets):
    pass