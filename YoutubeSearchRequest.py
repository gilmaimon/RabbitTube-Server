from YoutubeCommon import *
from YoutubeSearchResponse import *

## Precondition Constants
MAXIMUM_SEARCH_LIMIT = 100
MINIMUM_SEARCH_LIMIT = 10

# Class for representing an executable youtube search query
# The search is universal for both playlists, videos or both
class YoutubeSearchRequest:
        def __init__(self, youtubeApiKey, searchQuery, numOfResults, requestedItemsType, pageToken = None):
                assert(numOfResults >= MINIMUM_SEARCH_LIMIT and numOfResults <= MAXIMUM_SEARCH_LIMIT)
                self.m_queryParameters = self.ConstructQueryParameters(youtubeApiKey, searchQuery, numOfResults, requestedItemsType, pageToken)

        async def ExecuteRequest(self):
                responseJson = await ExecuteRawJsonGetRequest(SEARCH_URL, self.m_queryParameters)
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
