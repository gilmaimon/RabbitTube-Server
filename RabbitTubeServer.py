from aiohttp import web
from YoutubeSongDownloader import *
from LocalStorage import *
from YoutubeSongSearch import *
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

def IsValidYoutubeURL(url):
	if not type(url) == type('string'): return False
	pattern = '^https:\/\/www\.youtube\.com\/watch\?v=([0-9a-zA-Z-_]{11})(&index=[0-9]*)?(&list=[0-9a-zA-Z-]*)?(&index=[0-9]*)?$'
	return re.match(pattern, url) != None

def IsValidRequestJSON(jsonDict):
	requiredParameters = [('url', type('str'))] #add any must-have parameters, tuple of param key and type needed
	for param in requiredParameters:
		if param[0] not in jsonDict: return False
		if type(jsonDict[param[0]]) != param[1]: return False
	return True

def YoutubeIdFromURL(url):
	pattern = 'watch\?v=([0-9a-zA-Z-_]{11})'
	results = re.findall(pattern, url)
	if len(results) == 0: return False
	return results[0]

class RabbitTubeServer:
	def __init__(self, videoDownloader, localStorage, songSearch, apiKey):
		self.m_videoDownloader = videoDownloader
		self.m_localStorage = localStorage
		self.m_songSearch = songSearch
		self.m_apiKey = apiKey

	def GetErrorResponseForDownloadRequest(self, requestJson, responseJson):
		#no json param supplied
		if requestJson == None:
			return BuildErrorResponse(responseJson, message = 'invalid or no json param on key: \'data\'')

		#case of missing params or params of the wrong type
		if not IsValidRequestJSON(requestJson):
			return BuildErrorResponse(responseJson, message = 'Some must-have parameters are missing or of wrong type (\'url\' maybe?).')
		return None


	async def HandleDownloadRequest(self, request):
		responseJson = { 'error': False, 'message': None, 'downloadPath': None }

		try:
			requestJson = await request.json()
		except:
			return BuildErrorResponse(responseJson, message = 'request json is badly formatted')

		errorResponse = self.GetErrorResponseForDownloadRequest(requestJson, responseJson)
		#in case of error, return the error response indicating the problem for the client
		if errorResponse != None:
			return errorResponse

		url = requestJson['url']
		#if the video url is incorrect
		if not IsValidYoutubeURL(url):
			return BuildErrorResponse(responseJson, message = 'the supplied url is invalid.')

		videoID = YoutubeIdFromURL(url)
		gotFile = self.m_videoDownloader.DownloadSong(videoID)
		if not gotFile:
			return BuildErrorResponse(responseJson, message = 'could not download the video.')
		pathToFile = self.m_localStorage.GetFilePath(videoID)
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
server = RabbitTubeServer(YoutubeSongDownloader(localStorage), localStorage, YoutubeSongSearch(), YOUTUBE_APIKEY)

app = web.Application()
app.router.add_post('/download/song', server.HandleDownloadRequest)
app.router.add_post('/search/videos', server.HandleSearchVideosRequest)
app.router.add_post('/search/songs', server.HandleSearchVideosRequest)
web.run_app(app, port=8080)
