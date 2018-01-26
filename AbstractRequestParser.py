from abc import ABC
from abc import abstractmethod

# class for reciving a request object and return a dictinary with the request parameters
class AbstractRequestParser(ABC):

	def __init__(self):
		super().__init__()
		#self.m_error = error
		
	@abstractmethod
	def GetRequestParams(self, request):
		pass
