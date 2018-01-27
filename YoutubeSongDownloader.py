# ------------ YoutubeSongDownloader ------------

from AbstractSongDownloader import *
from subprocess import call

# This class is responsible for downloading song from
# youtube. current implementaion is using youtube-dl
class YoutubeSongDownloader(AbstractSongDownloader):

	def __init__(self, localStorage):
		super().__init__(localStorage)

	@staticmethod
	def __GetYoutubeDlOptions():
		ydlOptions = ['--no-playlist', '--no-check-certificate', '-x', '--audio-format', 'mp3', '-o', self.GetLocalStorage().GetCacheDirectory() + '/%(id)s.%(ext)s', '--']
		return ydlOptions

	# Download the song into local storage and return whether 
	# The song is available to acces via local storage (either if its already
	# exist or successfully downloaded)
	def DownloadSong(self, songId):
		if self.GetLocalStorage().IsSongInLocalStorage(songId):
			return True

		call(['youtube-dl'] + self.__GetYoutubeDlOptions() + [songId])
		return self.GetLocalStorage().IsSongInLocalStorage(songId)