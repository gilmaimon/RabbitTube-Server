from AbstractSongDownloader import *
from subprocess import call

class YoutubeSongDownloader(AbstractSongDownloader):

	def __init__(self, localStorage):
		super().__init__(localStorage)

	def GetYoutubeDlOptions(self):
		ydlOptions = ['--no-playlist', '--no-check-certificate', '-x', '--audio-format', 'mp3', '-o', self.GetLocalStorage().GetCacheDirectory() + '/%(id)s.%(ext)s', '--']
		return ydlOptions

	def DownloadSong(self, id):
		# isValidId
		# doesYoutubeFileExist
		if self.GetLocalStorage().IsSongInLocalStorage(id):
			return True

		call(['youtube-dl'] + self.GetYoutubeDlOptions() + [id])
		return self.GetLocalStorage().IsSongInLocalStorage(id)

#ysd = YoutubeSongDownloader(tempLocalStorage())
#ysd.DownloadSong("SDTHunBmslc")

