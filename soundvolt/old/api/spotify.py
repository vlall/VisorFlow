import json
import urllib2
from print_function.printpretty import prettyPrint

class Spotify:

	def __init__(self, name):
		json_data = urllib2.urlopen('https://ws.spotify.com/search/1/track.json?q=%s' % (name))
		self.data = json.load(json_data)
		json_data.close()  
		self.name = name

	def display_name(self):
		return self.name

	def spotify_tags(self):
		return self.data['info']

	def spotify_artist_stats(self):
		return self.data['artist']['stats']['listeners']

	def spotify_playcount(self):
		return self.data['artist']['stats']['playcount']
		
if __name__ == '__main__':
	artist = Spotify('cher')
	print artist.display_name() 
	print artist.spotify_tags()
	printpretty.prettyPrint(artist.data)  

