import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def users():
    raw_tweets = get_raw_tweets()
    users = pd.json_normalize(raw_tweets['user'])
    users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)
    users = pd.DataFrame(users)
    users.drop_duplicates(subset=['userId'], inplace=True)
    return users

def tweets():
    raw_tweets = get_raw_tweets()
    user_id = []
    for user in raw_tweets['user']:
        uid = user['id']
        user_id.append(uid)
    raw_tweets['userId'] = user_id
    tweets = raw_tweets
    tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)
    return tweets

def get_raw_tweets():
    return pd.read_json('farmers-protest-tweets.json', lines=True)