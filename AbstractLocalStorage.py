# ------------- AbstractLocalStorage -------------

from abc import ABC
from abc import abstractmethod

class AbstractLocalStorage(ABC):

	def __init__(self):
		super().__init__()

	@abstractmethod
    def GetCacheDirectory(self):
            pass

	@abstractmethod
    def IsSongInLocalStorage(self, id):
            pass

	@abstractmethod
    def GetFilePath(self, id):
            pass