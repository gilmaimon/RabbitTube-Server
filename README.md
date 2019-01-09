# RabbitTube-Server
server code used for RabbitTube app (app for downloading and searching youtube videos as songs)
# RabbitTube-Server
Server used for RabbitTube app (app for downloading and searching youtube videos as songs)

# Requirements
- Python3
- [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
- [youtube-dl](https://rg3.github.io/youtube-dl/)
- [aria2c](https://aria2.github.io/)

# Usage
### Searching Youtube Songs
```JSON
Method: POST
Path: '/search/songs'
Body:
{
    "query": "SOME_QUERY_STRING"
}
```
Assuming the request is valid, the server response will be:
```JSON
{
   "prevPageToken":null,
   "items":[
      {
         "thumbnails":{
            "high":{
               "url":"https://i.ytimg.com/vi/vhMlaCdlLbc/mqdefault.jpg",
               "height":180,
               "width":320
            },
            "default":{
               "url":"https://i.ytimg.com/vi/vhMlaCdlLbc/mqdefault.jpg",
               "height":180,
               "width":320
            }
         },
         "title":"Khesari Lal Yadav - Bandhan - Bhojpuri  Songs 2015 new",
         "videoID":"vhMlaCdlLbc",
         "channelTitle":"Wave Music",
         "description":"Subscribe Now:- http://goo.gl/ip2lbk..."
      },
      {...},
      {...},
      ...
    ]
}

```

### Downloading a Youtube Song
Request:
```JSON
Method: POST
Path: '/download/song'
Body:
{
    "url": "VALID_YOUTUBE_VIDEO_URL"
}
```

Response: 
The server will respond with either the mp3 file or an error message.
In case of an error message the Content-Type header will be `application/json` and for success it will be `audio/mpeg`.
