#YoutubeRequestProccessor
from AbstractRequestProccessor import *

class YoutubeRequestProccessor(AbstractRequestProccessor):
	def __init__(self, validator):
		AbstractRequestProccessor.__init__(self, validator)

	def YoutubeIdFromURL(url):
		pattern = 'watch\?v=([0-9a-zA-Z-_]{11})'
		results = re.findall(pattern, url)
		if len(results) == 0: return False
		return results[0]

	@abstractmethod
	def ExtractIdFromDownloadRequestParams(self, params):
		try:
			url = params['url']
			return False, YoutubeIdFromURL(url)
		except:
			return True, None