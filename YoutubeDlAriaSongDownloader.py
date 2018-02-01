# ------------ YoutubeDlAriaSongDownloader ------------

from AbstractSongDownloader import *
from subprocess import call
import threading


class DownloadTask():
	def __init__(self, command_line_arguments):
		self.__args = command_line_arguments
	
	def run(self):
		call(self.__args)

# This class is responsible for downloading song from
# youtube. current implementaion is using youtube-dl
class YoutubeDlAriaSongDownloader(AbstractSongDownloader):
	
	def __init__(self, localStorage):
		super().__init__(localStorage)

	def __GetYoutubeDlOptions(self):
		ydlOptions = [
			'--no-playlist',
			'--no-check-certificate',
			'-x', '--audio-format', 'mp3',
			'-o', self.GetLocalStorage().GetCacheDirectory() + '/%(id)s.%(ext)s',
			'--external-downloader', 'aria2c',
			#'--external-downloader-args','\"-x 16 -s 16 -k 1M\"',
			'--'
		]
		return ydlOptions

	# Download the song into local storage and return whether 
	# The song is available to acces via local storage (either if its already
	# exist or successfully downloaded)
	def DownloadSong(self, songId):
		if self.GetLocalStorage().IsSongInLocalStorage(songId):
			return True

		#download the song
		downloadTask = DownloadTask(['youtube-dl'] + self.__GetYoutubeDlOptions() + [songId])
		downloadTask.run();

		return self.GetLocalStorage().IsSongInLocalStorage(songId)
