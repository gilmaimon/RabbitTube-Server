#YoutubeRequestValidator

from AbstractRequestValidator import *
import re

class YoutubeRequestValidator(AbstractRequestValidator):
	def __init__(self):
		AbstractRequestValidator.__init__(self)

	@staticmethod
	def IsValidYoutubeURL(url):
		if not type(url) == type('string'): return False
		pattern = '^https:\/\/www\.youtube\.com\/watch\?v=([0-9a-zA-Z-_]{11})(&index=[0-9]*)?(&list=[0-9a-zA-Z-]*)?(&index=[0-9]*)?$'
		return re.match(pattern, url) != None

	@staticmethod
	def IsValidDownloadRequestJSON(jsonDict):
		requiredParameters = [('url', type('str'))] #add any must-have parameters, tuple of param key and type needed
		for param in requiredParameters:
			if param[0] not in jsonDict: return False
			if type(jsonDict[param[0]]) != param[1]: return False
		return True

	def AreDownloadRequestParamsValid(self, params):
		if self.IsValidDownloadRequestJSON(params) == False:
			return False
		url = params['url']
		if self.IsValidYoutubeURL(url) == False:
			return False
		else:
			return True	
	
	@staticmethod
	def IsValidYoutubeQuery(query):
		if not type(query) == type('string'): return False
		return len(query) <= 75 and len(query) > 0

	@staticmethod
	def IsValidSearchQueryParams(jsonDict):
		requiredParameters = [('query', type('str'))] #add any must-have parameters, tuple of param key and type needed
		for param in requiredParameters:
			if param[0] not in jsonDict: return False
			if type(jsonDict[param[0]]) != param[1]: return False

		return True

	def AreSearchRequestParamsValid(self, params):
		if self.IsValidSearchQueryParams(params) == False:
			return False

		query = params['query']
		if self.IsValidYoutubeQuery(query) == False:
			return False
		else:
			return True	
				
