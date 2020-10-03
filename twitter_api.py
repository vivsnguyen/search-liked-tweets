from __future__ import absolute_import, print_function
import tweepy

import os
import requests
import json

# header_info = {
#     'oauth_consumer_key': os.environ['TWITTER_API_KEY'],
#     'oauth_consumer_secret': os.environ['TWITTER_API_KEY_SECRET'],
#     'oauth_token': os.environ['TWITTER_ACCESS_TOKEN'],
#     'oauth_token_secret': os.environ['TWITTER_ACCESS_TOKEN_SECRET']
# }

dane_user = 'danusinmyanus'

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_KEY_SECRET']

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)


# def get_likes_list(screen_name):
#     """
#     """

#     url = 'https://api.twitter.com/1.1/favorites/list.json'

#     params_info = {'screen_name': screen_name, 'count': 5}

#     response = requests.get(url,params=params_info,headers=header_info).json()
    
#     return response

def get_likes_list(username):
    """
    Returns .

    Parameters:	
    username
    
    Return type:	
    a list of dictionaries containing status info
    """
    likes_list = []

    for status in api.favorites(username):
        json_str = json.dumps(status._json)
        status_json = json.loads(json_str)

        likes_list.append(status_json)
    return likes_list


def search():
    """
    """
    pass


# how to access favorites url to embed