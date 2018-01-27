# ------------ YoutubeRequestValidator ------------

from AbstractRequestValidator import *
import re

# Class for validating parameters given to the server,
# Making sure that the mandatory keys exist and that the value 
# paired with those keys are of the correct type and whithin the allowed input-range
class YoutubeRequestValidator(AbstractRequestValidator):
	def __init__(self):
		AbstractRequestValidator.__init__(self)

	@staticmethod
	def __IsValidYoutubeURL(url):
		if not type(url) == type('string'): return False
		pattern = '^https:\/\/www\.youtube\.com\/watch\?v=([0-9a-zA-Z-_]{11})(&index=[0-9]*)?(&list=[0-9a-zA-Z-]*)?(&index=[0-9]*)?$'
		return re.match(pattern, url) != None

	@staticmethod
	def __IsValidDownloadRequestJSON(jsonDict):
		requiredParameters = [('url', type('str'))]
		for param in requiredParameters:
			if param[0] not in jsonDict: return False
			if type(jsonDict[param[0]]) != param[1]: return False
		return True

	def AreDownloadRequestParamsValid(self, params):
		if self.__IsValidDownloadRequestJSON(params) == False:
			return False
		url = params['url']
		if self.__IsValidYoutubeURL(url) == False:
			return False
		else:
			return True	
	
	@staticmethod
	def __IsValidYoutubeQuery(query):
		if not type(query) == type('string'): return False
		return len(query) <= 75 and len(query) > 0

	@staticmethod
	def __IsValidSearchQueryParams(jsonDict):
		requiredParameters = [('query', type('str'))] 
		for param in requiredParameters:
			if param[0] not in jsonDict: return False
			if type(jsonDict[param[0]]) != param[1]: return False

		return True

	def AreSearchRequestParamsValid(self, params):
		if self.__IsValidSearchQueryParams(params) == False:
			return False

		query = params['query']
		if self.__IsValidYoutubeQuery(query) == False:
			return False
		else:
			return True	
				
