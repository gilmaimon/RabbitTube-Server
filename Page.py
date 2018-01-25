class Page:
	def __init__(self, totalAvailableResults, numResults, nextPageToken, prevPageToken):
		self.m_totalAvailableResults = totalAvailableResults,
		self.m_numResults = numResults
		self.m_nextPageToken = nextPageToken
		self.m_prevPageToken = prevPageToken
		self.m_items = []

	@classmethod
	def fromDict(self, dataAsDict):
		totalAvailableResults = dataAsDict['totalResults']
		numResults = dataAsDict['resultsShowing']
		nextPageToken = dataAsDict['nextPageToken']
		prevPageToken = dataAsDict['prevPageToken']
		newInstance = self(totalAvailableResults, numResults, nextPageToken, prevPageToken)
		return newInstance

	def AddItem(self, item):
		self.m_items += [item]

	def GetItems(self):
		return self.m_items

	def SetItems(self, items):
		self.m_items = items

	def AsDict(self):
		result = {}
		result['totalResults'] = self.m_totalAvailableResults
		result['resultsShowing'] = self.m_numResults
		result['nextPageToken'] = self.m_nextPageToken
		result['prevPageToken'] = self.m_prevPageToken
		result['items'] = []
		for item in self.m_items:
			result['items'] += [item.AsDict()]
		return result

