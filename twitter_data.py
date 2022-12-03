import configparser
import tweepy
import json
from tweepy.auth import OAuthHandler

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_secret = config['twitter']['api_key_secret']
acces_token = config['twitter']['access_token']
acces_secret = config['twitter']['access_token_secret']

authentication = tweepy.OAuthHandler(api_key, api_secret)
authentication.set_access_token(acces_token, acces_secret)

api = tweepy.API(authentication, parser=tweepy.parsers.JSONParser())

def get_user(username):
    return api.get_user(screen_name=username)

def get_user_timeline(username):
    data = []

    for tweet in tweepy.Cursor(api.user_timeline, screen_name = username, exclude_replies = True, include_rts = False, tweet_mode = 'extended').items():
        data.append([username, tweet.full_text, tweet.favourite_count, tweet.retweet_count])
    
    return data