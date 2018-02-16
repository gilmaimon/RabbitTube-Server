from aiohttp import web
import asyncio

from AbstractSongDownloader import AbstractSongDownloader
from AbstractLocalStorage import AbstractLocalStorage
from AbstractSongSearch import AbstractSongSearch
from AbstractRequestParser import AbstractRequestParser
from AbstractRequestProccessor import AbstractRequestProccessor

from concurrent.futures import ThreadPoolExecutor

NUM_THREADS_IN_POOL = 10

class RabbitTubeServer:
	def __init__(self, songDownloader, localStorage, songSearch, requestParser, requestProccessor):
		isinstance(songDownloader, AbstractSongDownloader)
		isinstance(localStorage, AbstractLocalStorage)
		isinstance(songSearch, AbstractSongSearch)
		isinstance(requestParser, AbstractRequestParser)
		isinstance(requestProccessor, AbstractRequestProccessor)

		self.__loop =  asyncio.get_event_loop()
		self.__executor = ThreadPoolExecutor(NUM_THREADS_IN_POOL)
		self.__songDownloader = songDownloader
		self.__localStorage = localStorage
		self.__songSearch = songSearch
		self.__requestParser = requestParser
		self.__requestProccessor = requestProccessor

		self.__app = web.Application()
		self.__InitRoutes()


	def __InitRoutes(self):
		self.__app.router.add_post('/download/song', self.HandleDownloadRequest)
		self.__app.router.add_post('/search/videos', self.HandleSearchVideosRequest)
		self.__app.router.add_post('/search/songs', self.HandleSearchVideosRequest)

	def Start(self, portNumber):
		web.run_app(self.__app, port = portNumber)

	@staticmethod
	def __BuildErrorResponse(message = 'Unknown input error'):
		responseJson = {}
		responseJson['error'] = True
		responseJson['message'] = message
		return web.json_response(responseJson)

	async def HandleDownloadRequest(self, request):
		responseJson = { 'error': False, 'message': None, 'downloadPath': None }

		# Proccess the web request and extract the parameters
		errorWhileParsingRequest, requestParameters = await self.__requestParser.GetRequestParams(request)
		if errorWhileParsingRequest:
			return self.__BuildErrorResponse(message = 'error while parsing request')

		# Are the request Parameters ok? get the song to be downloaded
		requestValidationError, songId = self.__requestProccessor.TryExtractIdFromDownloadRequestParams(requestParameters)
		if requestValidationError:
			return self.__BuildErrorResponse(message = 'error while getting song id from request')

		# Try to download and return the song to the client
		gotFile = await self.__loop.run_in_executor(self.__executor, self.__songDownloader.DownloadSong, songId)
		if not gotFile:
			return self.__BuildErrorResponse(message = 'could not download the song.')
		pathToFile = self.__localStorage.GetFilePath(songId)

		return web.FileResponse(pathToFile)

	async def HandleSearchVideosRequest(self, request):
		# Proccess the web request and extract the parameters
		errorWhileParsingRequest, requestParameters = await self.__requestParser.GetRequestParams(request)
		if errorWhileParsingRequest:
			return self.__BuildErrorResponse(message = 'error while parsing request')

		# Are the request Parameters ok? get the song to be downloaded
		requestValidationError, query = self.__requestProccessor.TryExtractQueryFromSearchRequestParams(requestParameters)
		if requestValidationError:
			return self.__BuildErrorResponse(message = 'error while getting query from request')

		# Perform the query and return the results
		pageResult = await self.__songSearch.SearchSongs(query)
		jsonResult = pageResult.AsDict()

		return web.json_response(jsonResult)
