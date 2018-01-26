#AbstractRequestValidator

from abc import ABC
from abc import abstractmethod

# class for reciving a request object and return a dictinary with the request parameters
class AbstractRequestValidator(ABC):

	def __init__(self):
		super().__init__()
	
	@abstractmethod
	def AreDownloadRequestParamsValid(self, params):
		pass