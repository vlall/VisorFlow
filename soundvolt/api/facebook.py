import json
import urllib2
from print_function import prettyprint

class Facebook:

	def __init__(self, name):
		json_data = urllib2.urlopen('https://graph.facebook.com/%s' % (name))
		self.data = json.load(json_data)
		json_data.close()  
		self.name = name

	def display_name(self):
		return self.name

	def get_likes(self):
		#You could do https://graph.facebook.com/%s?fields=likes
		return self.data['likes']

	def get_talking(self):
		return self.data['talking_about_count']

	def get_genre(self):
		return self.data['genre']

	def get_hometown(self):
		return self.data['hometown']

	def get_label(self):
		return self.data['record_label']

	def get_link(self):
		return self.data['link']

	def get_id(self):
		return self.data['id']	

if __name__ == '__main__':
	artist = Facebook('lilwayne')
	print artist.display_name() 
	print artist.get_likes()
	print artist.get_genre()
	#prettyprint.prettyPrint(artist.data)  

