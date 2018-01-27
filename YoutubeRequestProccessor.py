# ------------ YoutubeRequestProccessor ------------

from AbstractRequestProccessor import *
import re 

# Class for processing and validating parsed parameters
class YoutubeRequestProccessor(AbstractRequestProccessor):
	def __init__(self, validator):
		AbstractRequestProccessor.__init__(self, validator)

	@staticmethod
	def YoutubeIdFromURL(url):
		pattern = 'watch\?v=([0-9a-zA-Z-_]{11})'
		results = re.findall(pattern, url)
		if len(results) == 0: return False
		return results[0]

	def __ExtractIdFromDownloadRequestParams(self, params):
		url = params['url']
		return False, self.YoutubeIdFromURL(url)

	def __ExtractQueryFromSearchRequestParams(self, params):
		query = params['query']
		return False, query