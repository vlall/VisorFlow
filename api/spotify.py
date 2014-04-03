import json
import urllib2


'''
Filler data below, will fix tomorrow.
'''

json_data = urllib2.urlopen('https://ws.spotify.com/search/1/track.json?q=%s' % (userName))
data = json.load(json_data)
json_data.close()

def spotify():
	return data['top']

def spotify_artist_stats(userName):
	return data['artist']['stats']['listeners']

def spotify_playcount(userName):
	return data['artist']['stats']['playcount']
	
if __name__ == '__main__':
	print spotify_artist_stats('cher')
