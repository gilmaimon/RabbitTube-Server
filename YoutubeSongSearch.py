from AbstractSongSearch import AbstractSongSearch
from YoutubeSearchRequest import *
from YoutubeCommon import *

DEFAULT_NUM_RETURN_ITEMS = 35

class YoutubeSongSearch(AbstractSongSearch):
	def __init__(self, apikey):
		AbstractSongSearch.__init__(self)
		self.m_apiKey = apikey

	def SearchSongs(self, query):
		searchRequest = YoutubeSearchRequest(self.m_apiKey, query, DEFAULT_NUM_RETURN_ITEMS,TYPE_VIDEO)
		return searchRequest.ExecuteRequest()
