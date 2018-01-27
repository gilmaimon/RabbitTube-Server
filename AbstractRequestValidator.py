# ----------- AbstractRequestValidator -----------

from abc import ABC
from abc import abstractmethod

# This class is responsible for validating paremeters 
# parsed from a request object. Do they contain all 
# the needed information and meet the requirements
class AbstractRequestValidator(ABC):

	def __init__(self):
		super().__init__()
	
	@abstractmethod
	def AreDownloadRequestParamsValid(self, params):
		pass

	@abstractmethod
	def AreSearchRequestParamsValid(self, params):
		pass
		