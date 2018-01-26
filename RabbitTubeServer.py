from aiohttp import web
from YoutubeSongDownloader import *
from LocalStorage import *
from YoutubeSongSearch import *
from YoutubeRequestValidator import *
from YoutubeRequestProccessor import *
import re

def IsValidYoutubeQuery(query):
	if not type(query) == type('string'): return False
	return len(query) <= 75 and len(query) > 0

def IsValidSearchQueryJSON(jsonDict):
	requiredParameters = [('query', type('str'))] #add any must-have parameters, tuple of param key and type needed
	for param in requiredParameters:
		if param[0] not in jsonDict: return False
		if type(jsonDict[param[0]]) != param[1]: return False

	return True

def BuildErrorResponse(responseJson, message = 'Unknown input error'):
	responseJson['error'] = True
	responseJson['message'] = message
	return web.json_response(responseJson)

class RabbitTubeServer:
	def __init__(self, videoDownloader, localStorage, songSearch, requestParser, requestProccessor, apiKey):
		self.m_videoDownloader = videoDownloader
		self.m_localStorage = localStorage
		self.m_songSearch = songSearch
		self.m_apiKey = apiKey
		self.m_requestParser = requestParser
		self.m_requestProccessor = requestProccessor

	async def HandleDownloadRequest(self, request):
		responseJson = { 'error': False, 'message': None, 'downloadPath': None }

		# Proccess the web request and extract the parameters
		errorWhileParsingRequest, requestParameters = self.m_requestParser.GetRequestParams(request)
		if errorWhileParsingRequest:
			return BuildErrorResponse(responseJson)

		# Are the request Parameters ok? get the song to be downloaded
		requestValidationError, songId = 
			self.requestProccessor.TryExtractIdFromDownloadRequestParams(requestParameters)
		if requestValidationError:
			return BuildErrorResponse(responseJson)

		# Try to download and return the song to the client
		gotFile = self.m_videoDownloader.DownloadSong(songId)
		if not gotFile:
			return BuildErrorResponse(responseJson, message = 'could not download the song.')
		pathToFile = self.m_localStorage.GetFilePath(songId)
		
		return web.FileResponse(pathToFile)

	async def HandleSearchVideosRequest(self, request):
		responseJson = { 'error': False, 'message': None }
		requestJson = None
		try:
			requestJson = await request.json()
		except:
			return BuildErrorResponse(responseJson, message = 'request json is badly formatted')

		if requestJson == None or not IsValidSearchQueryJSON(requestJson):
			return BuildErrorResponse(responseJson, message = 'missing query for the search')
		pageToken = None
		query = requestJson['query']
		if not IsValidYoutubeQuery(query): return BuildErrorResponse(responseJson, message = 'bad query string. 75 >= len > 0)')
		if 'pageToken' in requestJson:
			pageToken = requestJson['pageToken']
		pageResult = await self.m_songSearch.SearchSongs(query, self.m_apiKey)
		jsonResult = pageResult.AsDict()
		return web.json_response(jsonResult)

YOUTUBE_APIKEY = 'AIzaSyABJxY_QcTVLfjgwBffxP6w_AOWPc7LMyE'
localStorage = LocalStorage()
server = RabbitTubeServer(
	YoutubeSongDownloader(localStorage),
	localStorage,
	YoutubeSongSearch(),
	JsonRequestParser(),
	YoutubeRequestProccessor(YoutubeRequestValidator())
	YOUTUBE_APIKEY
)

app = web.Application()
app.router.add_post('/download/song', server.HandleDownloadRequest)
app.router.add_post('/search/videos', server.HandleSearchVideosRequest)
app.router.add_post('/search/songs', server.HandleSearchVideosRequest)
web.run_app(app, port=8080)
