# ------------ YoutubeSearchRequest ------------

from YoutubeCommon import *
from YoutubeSearchResponse import *

## Precondition Constants
MAX_SEARCH_LIMIT = 100
MIN_SEARCH_LIMIT = 10

# Class for representing an executable youtube search query
# The search is universal for both playlists, videos or both
class YoutubeSearchRequest:
        def __init__(self, youtubeApiKey, searchQuery, numOfResults, requestedItemsType, pageToken = None):
                assert(MIN_SEARCH_LIMIT <= numOfResults and numOfResults <= MAX_SEARCH_LIMIT)
                self.__queryParameters = self.ConstructQueryParameters(
                        youtubeApiKey,
                        searchQuery,
                        numOfResults,
                        requestedItemsType,
                        pageToken
                ) #end

        async def ExecuteRequest(self):
                responseJson = await ExecuteRawJsonGetRequest(SEARCH_URL, self.__queryParameters)
                parsedApiResponse = YoutubeSearchResponse(responseJson)
                return parsedApiResponse.Get()

        def ConstructQueryParameters(self, youtubeApiKey, searchQuery, numOfResults, requestedItemsType, pageToken):
                queryParameters = {
                        'q': searchQuery,
                        'part': 'snippet',
                        'maxResults': numOfResults,
                        'key': youtubeApiKey,
                        'topicId' : TOPIC_ID_MUSIC,
                        'type' : requestedItemsType
                }
                if pageToken != None:
                        queryParameters['pageToken'] = pageToken
                return queryParameters
