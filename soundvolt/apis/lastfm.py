import json
import urllib2

'''
this is for Top Artists:
http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=e72fac875761b48cd924e29014d89686&format=json&limit=6
'''

class Lastfm:

	def __init__(self, name):
		json_data = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=%s&api_key=2b35547bd5675d8ecb2b911ee9901f59&format=json' % (name))
		self.data = json.load(json_data)
		json_data.close()
		self.name = name

	def display_name(self):
		return self.name

	def lastfm_top():
		json_data = urllib2.urlopen('http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=e72fac875761b48cd924e29014d89686&format=json&limit=6')
		self.data = json.load(json_data)
		json_data.close()
		return self.data['top']

	def lastfm_stats(self):
		return self.data['artist']['stats']['listeners']

	def lastfm_playcount(self):
		return self.data['artist']['stats']['playcount']
	
if __name__ == '__main__':
	artist = Lastfm('cher')
	print "Name: " + artist.display_name() 
	print "Listeners: " + artist.lastfm_stats()
	print "Playcount: " + artist.lastfm_playcount()
	#prettyprint.prettyPrint(artist.data)  
