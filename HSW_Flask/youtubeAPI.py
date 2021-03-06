import pandas as pd
from youtube_api import YouTubeDataAPI

api_key = 'AIzaSyA0xZ5whsLAcleAFmDSwjwSUBaqX607GMs'

yt=YouTubeDataAPI(api_key)

tech_reviewer_search = yt.search(q='tech review', 
                          max_results = 5, 
                          order_by = 'viewCount', 
                          safe_search=None, 
                          relevance_language='en',
                          video_duration = 'any', 
                          search_type='channel')


print(tech_reviewer_search)