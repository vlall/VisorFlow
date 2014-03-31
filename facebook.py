import json
import urllib2

def fb_page_likes(userName):
  #You could do https://graph.facebook.com/%s?fields=likes
	json_data = urllib2.urlopen('https://graph.facebook.com/%s' % (userName))
	data = json.load(json_data)
	json_data.close()
	return data['likes']

print fb_page_likes('lilwayne')
