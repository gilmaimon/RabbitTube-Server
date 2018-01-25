from abc import ABC
from abc import abstractmethod

class AbstractSongSearch(ABC):

	def __init__(self):
		super().__init__()

	@abstractmethod
	def SearchSongs(self, query):
		pass
