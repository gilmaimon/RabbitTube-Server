from AbstractSongSearch import AbstractSongSearch
from YoutubeSearchRequest import *
from YoutubeCommon import *

DEFAULT_NUM_RETURN_ITEMS = 35

class YoutubeSongSearch(AbstractSongSearch):
	def __init__(self):
		AbstractSongSearch.__init__(self)

	def SearchSongs(self, query, apikey):
		searchRequest = YoutubeSearchRequest(apikey, query, DEFAULT_NUM_RETURN_ITEMS,TYPE_VIDEO)
		return searchRequest.ExecuteRequest()