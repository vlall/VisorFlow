import tweepy
import json

class twitterObj:

    # The consumer keys can be found on your application's details
    # page located at https://dev.twitter.com/apps (under "OAuth settings")
    def __init__(self, configPath='../../config.json' ):
        with open(configPath, 'r') as file:
            config = json.load(file)
        _consumer_key = config['consumer_key']
        _consumer_secret = config['consumer_secret']
        _access_token = config['access_token']
        _access_token_secret = config['access_token_secret']
        auth = tweepy.OAuthHandler(_consumer_key, _consumer_secret)
        auth.set_access_token(_access_token, _access_token_secret)
        self.api = tweepy.API(auth)

    def listFollowers(self, userName):  
        pass

if __name__ == '__main__':
    obama = twitterObj()
    user = obama.api.get_user('barackobama')
    # Do stuff
    print 'Handle: %s' % user.screen_name
    print 'Followers: %s'% user.followers_count