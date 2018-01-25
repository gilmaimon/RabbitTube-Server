from AbstractSongSearch import AbstractSongSearch
from YoutubeSearchRequest import *
from YoutubeCommon import *

DEFAULT_NUM_RETURN_ITEMS = 10

class YoutubeSongSearch(AbstractSongSearch):
	def __init__(self):
		AbstractSongSearch.__init__(self)

	def SearchSongs(self, query, apikey):
		searchRequest = YoutubeSearchRequest(apikey, query, DEFAULT_NUM_RETURN_ITEMS,TYPE_VIDEO)
		return searchRequest.ExecuteRequest()

#async def search():
#	search = YoutubeSongSearch()
#	resultPage = await search.SearchSongs("Meir Ariel", 'AIzaSyABJxY_QcTVLfjgwBffxP6w_AOWPc7LMyE')
#	print(resultPage.GetItems()[0].AsDict())
#
#import asyncio
#q = asyncio.Queue()
#loop = asyncio.get_event_loop()
#loop.create_task(search())
#loop.run_forever()
