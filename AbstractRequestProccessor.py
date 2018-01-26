#AbstractRequestProccessor

from abc import ABC
from abc import abstractmethod

# class for reciving a request object and return a dictinary with the request parameters
class AbstractRequestProccessor(ABC):

	def __init__(self, validator):
		super().__init__()
		self.m_validator = validator
		#self.m_error = error
	
	def TryExtractIdFromDownloadRequestParams(self, params):
		if self.m_validator.AreDownloadRequestParamsValid(params) == False:
			return True, None
		return self.ExtractIdFromDownloadRequestParams(params)

	def TryExtractQueryFromSearchRequestParams(self, params):
		if self.m_validator.AreSearchRequestParamsValid(params) == False:
			return True, None
		return self.ExtractQueryFromSearchRequestParams(params)

	@abstractmethod
	def ExtractIdFromDownloadRequestParams(self, params):
		pass

	@abstractmethod
	def ExtractQueryFromSearchRequestParams(self, params):
		pass
