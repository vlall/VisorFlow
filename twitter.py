import tweepy

def twitterFollowers(userName):  
  ## first set up authenticated API instance
  # The consumer keys can be found on your application's Details
  # page located at https://dev.twitter.com/apps (under "OAuth settings")
  consumer_key="XXXXXXX"
  consumer_secret="XXXXXXX"
  
  access_token="XXXXXXX"
  access_token_secret="XXXXXXX"
  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  
  followerCount = 0
  for block in tweepy.Cursor(api.followers_ids, 'userName').items():
  	followerCount+=1;
  return followerCount
