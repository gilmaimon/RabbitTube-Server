# ------------ YoutubeSearchResponse ------------

from YoutubeCommon import *
from Item import *
from Page import *

# Class for represnting a response that came back from youtube's api
# The class will parse the response to items contained in a page
class YoutubeSearchResponse:
	def __init__(self, responseJson):
		parsedResponse = self.ParseCommonSearchResponse(responseJson)
		self.__page = Page.fromDict(parsedResponse)
		items = self.ParseItems(responseJson['items'], ItemType.SONG)
		self.__page.SetItems(items)

	# Get the parsed page
	def Get(self):
		return self.__page

	# Youtube responses have metadata for wrapping a page of items (palylists or videos)
	# This routine parses those metadata items
	@staticmethod
	def ParseCommonSearchResponse(apiResultJson):
		parsedResult = {}
		# parse page info
		parsedResult['totalResults'] = apiResultJson['pageInfo']['totalResults']
		parsedResult['resultsShowing'] = apiResultJson['pageInfo']['resultsPerPage']

		#next page token is optional so parse if the result has it
		if 'nextPageToken' in apiResultJson:
			parsedResult['nextPageToken'] = apiResultJson['nextPageToken']
		else:
			parsedResult['nextPageToken'] = None

		#parse previous page token is optional aswell, parse it
		if 'prevPageToken' in apiResultJson:
			parsedResult['prevPageToken'] = apiResultJson['prevPageToken']
		else:
			parsedResult['prevPageToken'] = None

		return parsedResult

	@staticmethod
	def ParseItems(responseItems, itemsType):
		resultItems = []
		for rawItem in responseItems:
			#sometimes the api will return channels, in order to protect 
			#from failing to parse those items try-catch is used
			try:
				parsedItem = YoutubeSearchResponse.ParseResponseItem(rawItem, itemsType)
				resultItems += [Item.fromDict(parsedItem, itemsType)]
			except:
				pass
		return resultItems

	# Every item in the items returning from the youtube search api has alot of uneccessery data
    # This routine only takes the needed fields and returns a single parsed item
    # This routine will throw in case the item presented is not a youtube video or playlist item
    @staticmethod
	def ParseResponseItem(responseItem, itemType):
		item = {}
		if itemType == ItemType.SONG:
			item['type'] = 'video'
			item['videoID'] = responseItem['id']['videoId']
		elif itemType == ItemType.PLAYLIST:
			item['type'] = 'playlist'
			item['playlistID'] = responseItem['id']['playlistId']
		item['channelID'] = responseItem['snippet']['channelId']
		item['channelTitle'] = responseItem['snippet']['channelTitle']
		item['title'] = responseItem['snippet']['title']
		item['description'] = responseItem['snippet']['description']
		item['thumbnails'] = {}
		item['thumbnails']['default'] = responseItem['snippet']['thumbnails']['medium']
		item['thumbnails']['high'] = responseItem['snippet']['thumbnails']['high']
		return item


