import pandas as pd
#from youtube_api import YouTubeDataAPI
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json
from collections import OrderedDict
#from oauth2client.tools import argparser  oauth2 안씀

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class RefineChannelInfo: 

    def retrieveInfo(self, query, api_key):

        '''youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=api_key)

        # Call the search.list method to retrieve results matching the specified
        search_response = youtube.search().list(
            q=query,
            part="id,snippet",
            maxResults=5
        ).execute()'''

        # API 할당량을 위해 txt 파일에서 읽어서 진행
        content = ''
        with open('result.txt',mode="r",encoding='utf-8') as f:
            content = f.read()
        f.close()

        # 정제
        jsonResult = json.loads(content)
        itemResult = jsonResult['items']

        result = []
        for x in itemResult:
            info = x['snippet']

            title = info['title']
            thumbnails =  info['thumbnails']['default']['url']

            data = {
                'title' : title,
                'thumbnail' : thumbnails
            }

            result.append(json.dumps(data))

        print(result)

        resultJson = {
            'result' : result
        }

        #result = '{"title":"efefe" , "thumbnail": "aaa"}'
        return resultJson
                
        



