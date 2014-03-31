import json
import urllib2

'''
this is for Top Artists:
http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=e72fac875761b48cd924e29014d89686&format=json&limit=6
'''

json_data = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=%s&api_key=2b35547bd5675d8ecb2b911ee9901f59&format=json' % (userName))
data = json.load(json_data)
json_data.close()

def lastfm_top():
	json_data = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=e72fac875761b48cd924e29014d89686&format=json&limit=6')
	data = json.load(json_data)
	json_data.close()
	return data['top']

def lastfm_artist_Stats(userName):
	return data['artist']['stats']['listeners']

def lastfm_playcount(userName):
	return data['artist']['stats']['playcount']

print lastfm_artist_Stats('cher')
