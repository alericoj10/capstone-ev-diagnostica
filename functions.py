from audioop import reverse
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
    tweets['hastags'] = tweets['content'].apply(lambda x: [tag.strip("#") for tag in x.split() if tag.startswith("#")])
    hashtags_frecuency = {}
    for tags in tweets['hastags']:
        for tag in tags:
            if tag in hashtags_frecuency:
                hashtags_frecuency[tag] += 1
            else:
                hashtags_frecuency[tag] = 1
    hashtags_frecuency = {k: v for k, v in sorted(hashtags_frecuency.items(), key=lambda item: item[1], reverse=True)}
    top_10_dict = {}
    n = 1
    while n < 10:
        for k, v in hashtags_frecuency.items():
            top_10_dict[k] = v
            n += 1
    return top_10_dict
