from aiohttp import web

from YoutubeSongDownloader import *
from TmpLocalStorage import *
from YoutubeSongSearch import *
from YoutubeRequestValidator import *
from YoutubeRequestProccessor import *
from JsonRequestParser import *

from RabbitTubeServer import RabbitTubeServer

YOUTUBE_APIKEY = 'AIzaSyABJxY_QcTVLfjgwBffxP6w_AOWPc7LMyE'
def main():
	localStorage = TmpLocalStorage()
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

if __name__ == '__main__':
	main()
