# ------------- JsonRequestParser -------------

from AbstractRequestParser import *

# Implemenation for getting parameters out of a request object
class JsonRequestParser(AbstractRequestParser):
	def __init__(self):
		super().__init__()

	async def GetRequestParams(self, request):
		params = {}
		error = False
		try:
			params = await request.json()
			if params == None: 
				error = True
		except:
			error = True

		return error, params
