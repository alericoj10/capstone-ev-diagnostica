import re
import pandas as pd

def most_retweeted(tweets):
    top_tweets = tweets.sort_values(by="retweetCount", ascending=False).head(10)
    return top_tweets[['content', 'retweetCount']]

def most_active_users(tweets, users):
    user_ids = tweets['userId'].value_counts().head(10)
    top_users = users.loc[users['userId'].isin(user_ids.index.array)]
    return top_users[['username', 'displayname', 'userId']]

def most_active_days(tweets):
    tweets['date_day'] = tweets['date'].apply(lambda x: str(x).split(' ')[0])
    return tweets['date_day'].value_counts().head(10)

def most_frecuent_hashtags(tweets):
    pass