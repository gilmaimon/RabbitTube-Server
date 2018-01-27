# ----------- AbstractSongDownloader -----------

from abc import ABC
from abc import abstractmethod

# This class is responsible for downloading a song
# given a unique song-identifier and a local storage 
# for checking if the song is already downloaded
# and in case it is not, where to store the downloaded item 
class AbstractSongDownloader(ABC):

	def __init__(self, localStorage):
		super().__init__()
		self.__localStorage = localStorage

	def GetLocalStorage(self):
		return self.__localStorage

	@abstractmethod
	def DownloadSong(self, id):
		pass
