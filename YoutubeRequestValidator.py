#YoutubeRequestValidator

from AbstractRequestValidator import *

class YoutubeRequestValidator(AbstractRequestValidator):
	def __init__(self):
		AbstractRequestProccessor.__init__(self)


	def IsValidYoutubeURL(url):
		if not type(url) == type('string'): return False
		pattern = '^https:\/\/www\.youtube\.com\/watch\?v=([0-9a-zA-Z-_]{11})(&index=[0-9]*)?(&list=[0-9a-zA-Z-]*)?(&index=[0-9]*)?$'
		return re.match(pattern, url) != None

	def IsValidDownloadRequestJSON(jsonDict):
		requiredParameters = [('url', type('str'))] #add any must-have parameters, tuple of param key and type needed
		for param in requiredParameters:
			if param[0] not in jsonDict: return False
			if type(jsonDict[param[0]]) != param[1]: return False
		return True

	def AreDownloadRequestParamsValid(self, params):
		if IsValidDownloadRequestJSON(params) == False:
			return False
		url = params['url']
		if IsValidYoutubeURL(url) == False:
			return False
		else:
			return True		