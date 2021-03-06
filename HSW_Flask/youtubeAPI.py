import pandas as pd
from youtube_api import YouTubeDataAPI

api_key = ''

yt=YouTubeDataAPI(api_key)

tech_reviewer_search = yt.search(q='보겸TV', 
                          max_results = 5, 
                          order_by = 'viewCount', 
                          safe_search=None, 
                          relevance_language='en',
                          video_duration = 'any', 
                          search_type='channel')


print(tech_reviewer_search)