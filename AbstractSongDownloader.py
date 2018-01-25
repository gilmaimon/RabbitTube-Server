from abc import ABC
from abc import abstractmethod

class AbstractSongDownloader(ABC):

	def __init__(self, localStorage):
		super().__init__()
		self.m_localStorage = localStorage

	def GetLocalStorage(self):
		return self.m_localStorage

	@abstractmethod
	def DownloadSong(self, id):
		pass
