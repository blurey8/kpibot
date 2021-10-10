#!/usr/bin/env python
from os import environ as env
import tweepy


# Authenticate to Twitter
auth = tweepy.OAuthHandler(env.get("API_KEY"), env.get("API_KEY_SECRET"))
auth.set_access_token(env.get("ACCESS_TOKEN"), env.get("ACCESS_TOKEN_SECRET"))

# Create API object
api = tweepy.API(auth)
try:
    api.verify_credentials()
    api.update_status("Test tweet from Tweepy Python")
    print("Authentication OK")
except:
    print("Error during authentication")
