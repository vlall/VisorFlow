import json
import urllib2

class Facebook:

	def __init__(self, name):
		json_data = urllib2.urlopen('https://graph.facebook.com/%s' % (name))
		self.data = json.load(json_data)
		json_data.close()  
		self.name = name
		data = self.data
		#You could do https://graph.facebook.com/%s?fields=likes
		self.likes = data['likes']
		self.talking =  data['talking_about_count']
		self.genre = data['genre']
		self.hometown = data['hometown']
		self.label = data['record_label']
		self.link = data['link']
		self.id = data['id']

if __name__ == '__main__':
	artist = Facebook('lilwayne')
	print artist.name
	print artist.likes
	print artist.genre

