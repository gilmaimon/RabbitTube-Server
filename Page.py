# This class represents a page of items
# each item is either a song or playlist 
class Page:
	def __init__(self, totalAvailableResults, numResults, nextPageToken, prevPageToken):
		self.__totalAvailableResults = totalAvailableResults
		self.__numResults = numResults
		self.__nextPageToken = nextPageToken
		self.__prevPageToken = prevPageToken
		self.__items = []

	@classmethod
	def fromDict(self, dataAsDict):
		totalAvailableResults = dataAsDict['totalResults']
		numResults = dataAsDict['resultsShowing']
		nextPageToken = dataAsDict['nextPageToken']
		prevPageToken = dataAsDict['prevPageToken']
		newInstance = self(totalAvailableResults, numResults, nextPageToken, prevPageToken)
		return newInstance

	def AddItem(self, item):
		self.__items += [item]

	def GetItems(self):
		return self.__items

	def SetItems(self, items):
		self.__items = items

	def AsDict(self):
		result = {}
		result['totalResults'] = self.__totalAvailableResults
		result['resultsShowing'] = self.__numResults
		result['nextPageToken'] = self.__nextPageToken
		result['prevPageToken'] = self.__prevPageToken
		result['items'] = []
		for item in self.__items:
			result['items'] += [item.AsDict()]
		return result

