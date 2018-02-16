from TmpLocalStorage 				import TmpLocalStorage
from YoutubeSongSearch 				import YoutubeSongSearch
from YoutubeRequestValidator 		import YoutubeRequestValidator
from YoutubeRequestProccessor		import YoutubeRequestProccessor
from JsonRequestParser 				import JsonRequestParser
from YoutubeDlAriaSongDownloader 	import YoutubeDlAriaSongDownloader

from RabbitTubeServer import RabbitTubeServer

YOUTUBE_APIKEY = 'AIzaSyABJxY_QcTVLfjgwBffxP6w_AOWPc7LMyE'
def main():
	localStorage = TmpLocalStorage()
	server = RabbitTubeServer (
		YoutubeDlAriaSongDownloader(localStorage),
		localStorage,
		YoutubeSongSearch(YOUTUBE_APIKEY),
		JsonRequestParser(),
		YoutubeRequestProccessor(YoutubeRequestValidator())
	)

	server.Start(8080)	

if __name__ == '__main__':
	main()
