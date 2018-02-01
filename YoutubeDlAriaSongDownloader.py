# ------------ YoutubeDlAriaSongDownloader ------------

from AbstractSongDownloader import *
from subprocess import call

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

		call(['youtube-dl'] + self.__GetYoutubeDlOptions() + [songId])
		return self.GetLocalStorage().IsSongInLocalStorage(songId)
