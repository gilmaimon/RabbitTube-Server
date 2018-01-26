#YoutubeRequestProccessor
from AbstractRequestProccessor import *
import re 

class YoutubeRequestProccessor(AbstractRequestProccessor):
	def __init__(self, validator):
		AbstractRequestProccessor.__init__(self, validator)

	@staticmethod
	def YoutubeIdFromURL(url):
		pattern = 'watch\?v=([0-9a-zA-Z-_]{11})'
		results = re.findall(pattern, url)
		if len(results) == 0: return False
		return results[0]


	def ExtractIdFromDownloadRequestParams(self, params):
#		try:
		url = params['url']
		return False, self.YoutubeIdFromURL(url)
#		except:
#			print('error in youtube request processor (url??)')
#			return True, None
