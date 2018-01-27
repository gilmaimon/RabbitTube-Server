# -------------- YoutubeSongSearch --------------

from AbstractSongSearch import AbstractSongSearch
from YoutubeSearchRequest import *
from YoutubeCommon import *

DEFAULT_NUM_RETURN_ITEMS = 35

# Class for searching youtube songs
class YoutubeSongSearch(AbstractSongSearch, apikey):
	def __init__(self):
		AbstractSongSearch.__init__(self)
		self.__apiKey = apikey

	# This function searches songs and returns them as a Page 
	def SearchSongs(self, query):
		searchRequest = YoutubeSearchRequest(self.__apiKey, query, DEFAULT_NUM_RETURN_ITEMS,TYPE_VIDEO)
		return searchRequest.ExecuteRequest()