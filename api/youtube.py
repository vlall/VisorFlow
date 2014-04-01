import json
import urllib2
from pprint import pprint

def yt_vid_info(videoID):	
	json_data = urllib2.urlopen('http://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=json' % (videoID))
	data = json.load(json_data)
	json_data.close()
	return data['entry']['yt$statistics']['viewCount']

#this is incorrect for now.
def yt_channel_info(channelName):	
	json_data= urllib2.urlopen('https://gdata.youtube.com/feeds/api/videos?q=%s&max-results=5&v=2&alt=jsonc&orderby=published' %(channelName))
	data = json.load(json_data)
	json_data.close()
	return data["entry"]['yt$statistics']['viewCount'][0]

#this is incorrect for now.
def yt_channel_uploads(channelName):
	json_data= urllib2.urlopen('http://gdata.youtube.com/feeds/api/users/%s/uploads?v=2&alt=jsonc' %(channelName))
	data = json.load(json_data)
	json_data.close()
	chanItems = len(["data"]['items'])
	for i in chanItems:
		viewCount = data["data"]['items'][i]['viewCount']
		viewCount+= int(viewCount)
	return viewCount
 
#Example pull:
print yt_vid_info('CwLuDO_Cxfc')
print yt_channel_uploads('smosh')
