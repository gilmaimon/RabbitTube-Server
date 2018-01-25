from YoutubeCommon import *
from Item import *
from Page import *

class YoutubeSearchResponse:
	def __init__(self, responseJson):
		parsedResponse = self.ParseCommonSearchResponse(responseJson)
		self.m_page = Page.fromDict(parsedResponse)
		items = self.ParseItems(responseJson['items'], ItemType.SONG)
		self.m_page.SetItems(items)

	def ParseItems(self, responseItems, itemType):
		resultItems = []
		for iItem in responseItems:
			#sometimes the api will return channels, in order to
			#protect from failing to parse those items im using try catch
			try:
				itemJson = self.ParseResponseItem(iItem, itemType)
				resultItems += [Item.fromDict(itemJson, itemType)]
			except e:
				pass
		return resultItems

	def Get(self):
		return self.m_page

	# Youtube responses have metadata for wrapping a page of items (palylists or videos)
	# This routine parses those metadata items
	def ParseCommonSearchResponse(self, apiResultJson):
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

	# Every item in the items returning from the youtube search api has alot of uneccessery data
        # This routine only takes the needed fields and returns a single parsed item
        # This routine will throw in case the item presented is not a youtube video or playlist item
	def ParseResponseItem(self, responseItem, itemType):
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


