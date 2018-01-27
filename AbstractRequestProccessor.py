# ----------- AbstractRequestProccessor -----------

from abc import ABC
from abc import abstractmethod

# this class gets the parsed request parameters and a validator.
# the class is responsible for validating and extracting needed data
# from the parsed request parameters
class AbstractRequestProccessor(ABC):

	def __init__(self, validator):
		super().__init__()
		self.__validator = validator
	
	# This routine will first validate the parsed parameters using a validator
	# Next the routine will try to extract the request data out of the params, in
	# this case, ID.
	# Return type: tuple(ErrorOcured(Boolean), String(Extracted Id))
	def TryExtractIdFromDownloadRequestParams(self, params):
		if self.__validator.AreDownloadRequestParamsValid(params) == False:
			return True, None
		return self._ExtractIdFromDownloadRequestParams(params)
	
	# This routine will first validate the parsed parameters using a validator
	# Next the routine will try to extract the request data out of the params, in
	# this case, Query String.
	# Return type: tuple(ErrorOcured(Boolean), String(Extracted Query))
	def TryExtractQueryFromSearchRequestParams(self, params):
		if self.__validator.AreSearchRequestParamsValid(params) == False:
			return True, None
		return self._ExtractQueryFromSearchRequestParams(params)

	@abstractmethod
	def _ExtractIdFromDownloadRequestParams(self, params):
		pass

	@abstractmethod
	def _ExtractQueryFromSearchRequestParams(self, params):
		pass
