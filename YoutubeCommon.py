import aiohttp
import json
import socket

async def ExecuteRawJsonGetRequest(url, params):
        conn = aiohttp.TCPConnector(family=socket.AF_INET)
        async with aiohttp.ClientSession(connector=conn) as session:
                        async with session.get(url, params = params) as resp:
                                responseText = await resp.text()
                                return json.loads(responseText)

# ------------------ Youtube Query Constants ------------------

# Youtube Allows Searching by topics, full topic-codes list at:
# https://gist.github.com/stpe/2951130dfc8f1d0d1a2ad736bef3b703
TOPIC_ID_MUSIC = '/m/04rlf'

# Youtube query types (for the results that will return)
TYPE_VIDEO = 'video'
TYPE_PLAYLIST = 'playlist'

# The youtube search API Endpoint
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

