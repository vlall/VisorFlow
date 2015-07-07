import json
import sys
import urllib2

class wikiObj:
	def __init__(self, name):
    		self.name = name
		try:
			json_data = urllib2.urlopen('https://en.wikipedia.org/w/api.php?format=json&action=query&titles=%s&prop=revisions&rvprop=content' % (name))
			self.data = json.load(json_data)
			json_data.close()
		except Exception:
			print 'JSON not being read!'

if __name__ == '__main__':
	country = wikiObj('bruno_mars')
	reload(sys)
   	sys.setdefaultencoding("utf-8")
	print(country.data)  
