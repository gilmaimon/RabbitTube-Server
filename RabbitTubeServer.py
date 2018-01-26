from aiohttp import web
from YoutubeSongDownloader import *
from LocalStorage import *
from YoutubeSongSearch import *
from YoutubeRequestValidator import *
from YoutubeRequestProccessor import *
from JsonRequestParser import *

class RabbitTubeServer:
	def __init__(self, videoDownloader, localStorage, songSearch, requestParser, requestProccessor):
		self.m_videoDownloader = videoDownloader
		self.m_localStorage = localStorage
		self.m_songSearch = songSearch
		self.m_requestParser = requestParser
		self.m_requestProccessor = requestProccessor

	@staticmethod
	def BuildErrorResponse(responseJson, message = 'Unknown input error'):
		responseJson['error'] = True
		responseJson['message'] = message
		return web.json_response(responseJson)

	async def HandleDownloadRequest(self, request):
		responseJson = { 'error': False, 'message': None, 'downloadPath': None }

		# Proccess the web request and extract the parameters
		errorWhileParsingRequest, requestParameters = await self.m_requestParser.GetRequestParams(request)
		if errorWhileParsingRequest:
			return self.BuildErrorResponse(responseJson, message = 'error while parsing request')

		# Are the request Parameters ok? get the song to be downloaded
		requestValidationError, songId = self.m_requestProccessor.TryExtractIdFromDownloadRequestParams(requestParameters)
		if requestValidationError:
			return self.BuildErrorResponse(responseJson, message = 'error while getting song id from request')

		# Try to download and return the song to the client
		gotFile = self.m_videoDownloader.DownloadSong(songId)
		if not gotFile:
			return self.BuildErrorResponse(responseJson, message = 'could not download the song.')
		pathToFile = self.m_localStorage.GetFilePath(songId)
		
		return web.FileResponse(pathToFile)

	async def HandleSearchVideosRequest(self, request):
		responseJson = { 'error': False, 'message': None }
		
		# Proccess the web request and extract the parameters
		errorWhileParsingRequest, requestParameters = await self.m_requestParser.GetRequestParams(request)
		if errorWhileParsingRequest:
			return self.BuildErrorResponse(responseJson, message = 'error while parsing request')

		# Are the request Parameters ok? get the song to be downloaded
		requestValidationError, query = self.m_requestProccessor.TryExtractQueryFromSearchRequestParams(requestParameters)
		if requestValidationError:
			return self.BuildErrorResponse(responseJson, message = 'error while getting query from request')

		# Perform the query and return the results
		pageResult = await self.m_songSearch.SearchSongs(query)
		jsonResult = pageResult.AsDict()

		return web.json_response(jsonResult)

YOUTUBE_APIKEY = 'AIzaSyABJxY_QcTVLfjgwBffxP6w_AOWPc7LMyE'
localStorage = LocalStorage()
server = RabbitTubeServer (
	YoutubeSongDownloader(localStorage),
	localStorage,
	YoutubeSongSearch(YOUTUBE_APIKEY),
	JsonRequestParser(),
	YoutubeRequestProccessor(YoutubeRequestValidator())
)

app = web.Application()
app.router.add_post('/download/song', server.HandleDownloadRequest)
app.router.add_post('/search/videos', server.HandleSearchVideosRequest)
app.router.add_post('/search/songs', server.HandleSearchVideosRequest)
web.run_app(app, port = 8080)
