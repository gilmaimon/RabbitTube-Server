# ------------- AbstractSongSearch -------------

from abc import ABC
from abc import abstractmethod

# This class is responsible for searching songs given a query
class AbstractSongSearch(ABC):

	def __init__(self):
		super().__init__()

	@abstractmethod
	def SearchSongs(self, query):
		pass
