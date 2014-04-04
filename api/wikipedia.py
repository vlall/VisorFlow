import json
import urllib2
from pprint import pprint

class WikiObject:

	def __init__(self, name):
		try:
			json_data = urllib2.urlopen('https://en.wikipedia.org/w/api.php?format=json&action=query&titles=%s&prop=revisions&rvprop=content' % (name) )
			self.data = json.load(json_data)
			json_data.close()
		except ValueError:
			print '********JSON not being read!!!!!**********'
		self.name = name

	def wiki_search(title):	
		return self.data['to']

	def display_name(self):
		return self.name

if __name__ == '__main__':
	artist = WikiObject('Chile')
	print artist.data
	#prettyprint.prettyPrint(artist.data)  
