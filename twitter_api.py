import os
import requests

header_info = {
    'oauth_consumer_key': os.environ['TWITTER_API_KEY'],
    'oauth_consumer_secret': os.environ['TWITTER_API_KEY_SECRET'],
    'oauth_token': os.environ['TWITTER_ACCESS_TOKEN'],
    'oauth_token_secret': os.environ['TWITTER_ACCESS_TOKEN_SECRET']
}

dane_user = 'danusinmyanus'

def get_liked_list(screen_name):
    """
    """
    url = 'https://api.twitter.com/1.1/favorites/list.json'

    params_info = {'screen_name': dane_user, 'count': 5}

    response = requests.get(url,params=params_info,headers=header_info).json()
    
    return response

def search():
    ""