import json
import urllib2
from pprint import pprint
from print_function import prettyprint

class Youtube(object):

	def __init__(self, name):
		#name
		self.name = name

	def display_name(self):
		return self.name

	def yt_vid_info(self, videoID):
		json_data = urllib2.urlopen('http://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=json' % (videoID))
		self.data = json.load(json_data)
		json_data.close()  	
		return self.data['entry']['yt$statistics']['viewCount']

	#fix the return
	def yt_channel_info(self, channelName):
		json_chan= urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?q=%s&max-results=5&v=2&alt=jsonc&orderby=published' %(channelName))
		self.chan = json.load(json_chan)
		json_chan.close() 	
		return self.chan["entry"]['yt$statistics']['viewCount'][0]

	#this is incorrect for now.
	def yt_channel_uploads(self, channelName):
		json_chan= urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?q=%s&max-results=5&v=2&alt=jsonc&orderby=published' %(channelName))
		self.chan = json.load(json_chan)
		json_chan.close() 
		json_data= urllib2.urlopen('http://gdata.youtube.com/feeds/api/users/%s/uploads?v=2&alt=jsonc' %(channelName))
		data = json.load(json_data)
		json_data.close()
		chanItems = len(["data"]['items'])
		for i in chanItems:
			viewCount = data["data"]['items'][i]['viewCount']
			viewCount+= int(viewCount)
		return viewCount
	 
#Example pull:
if __name__ == '__main__':
	artist = Youtube('John')
	print artist.yt_vid_info('CwLuDO_Cxfc')
	print artist.yt_channel_info('smosh')
	#prettyprint.prettyPrint(artist.data)  

