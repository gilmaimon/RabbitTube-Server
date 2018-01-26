from AbstractRequestParser import *

class JsonRequestParser(AbstractRequestParser):
	def __init__(self, request):
		super().__init__(request)

	def GetRequestParams(self, request):
		params = {}
		error = False
		try:
			params = await request.json()
			if params == None: 
				error = True
		except:
			error = True

		return error, params