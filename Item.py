from enum import Enum

class ItemType(Enum):
	SONG = 1
	PLAYLIST = 2

class Item:
	def __init__(self, id, title, subtitle, description, hq_thumbnail, itemType):
		self.m_id = id
		self.m_title = title
		self.m_subtitle = subtitle
		self.m_description = description
		self.m_hq_thumbnail = hq_thumbnail
		self.m_type = itemType

	@classmethod
	def fromDict(self, dataAsDict, itemType):
		subtitle = dataAsDict['channelTitle']
		title = dataAsDict['title']
		description = dataAsDict['description']
		hq_thumbnail = dataAsDict['thumbnails']['default']
		id = 'temp'
		if itemType == ItemType.SONG:
			id = dataAsDict['videoID']
		else:
			id = dataAsDict['playlistID']
		newInstance = self(id, title, subtitle, description, hq_thumbnail, itemType)
		return newInstance

	def GetId(self):
		return self.m_id

	def GetTitle(self):
		return self.m_title

	def AsDict(self):
		result = {}

		result['videoID'] = self.m_id
		result['channelTitle'] = self.m_subtitle
		result['title'] = self.m_title
		result['description'] = self.m_description

		result['thumbnails'] = {}
		result['thumbnails']['default'] = self.m_hq_thumbnail
		result['thumbnails']['high'] = self.m_hq_thumbnail
		return result
