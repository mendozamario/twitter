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