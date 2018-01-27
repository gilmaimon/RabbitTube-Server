from enum import Enum

class ItemType(Enum):
	SONG = 1
	PLAYLIST = 2

# This class is a unified represenation for playlist and song item
class Item:
	def __init__(self, id, title, subtitle, description, hq_thumbnail, itemType):
		self.__id = id
		self.__title = title
		self.__subtitle = subtitle
		self.__description = description
		self.__hq_thumbnail = hq_thumbnail
		self.__type = itemType

	@classmethod
	def fromDict(self, dataAsDict, itemType):
		subtitle = dataAsDict['channelTitle']
		title = dataAsDict['title']
		description = dataAsDict['description']
		hq_thumbnail = dataAsDict['thumbnails']['default']
		itemIdKey = None
		if itemType == ItemType.SONG:
			itemIdKey = dataAsDict['videoID']
		else:
			itemIdKey = dataAsDict['playlistID']
		newInstance = self(itemIdKey, title, subtitle, description, hq_thumbnail, itemType)
		return newInstance

	def GetId(self):
		return self.__id

	def GetTitle(self):
		return self.__title

	def AsDict(self):
		result = {}

		result['videoID'] = self.__id
		result['channelTitle'] = self.__subtitle
		result['title'] = self.__title
		result['description'] = self.__description

		result['thumbnails'] = {}
		result['thumbnails']['default'] = self.__hq_thumbnail
		result['thumbnails']['high'] = self.__hq_thumbnail
		return result
