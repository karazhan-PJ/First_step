from flask import Flask,request
from flask_restful import Resource, Api
from youtubeAPI import RefineChannelInfo
import numpy as np
import json

app = Flask(__name__)
api = Api(app)

class RetrieveChannelInfo(Resource):
    def get(self):
        
        print("aaa")
        print(request.values.getlist("query"))
        print("aab")
        
        
        #refineChannelInfo = RefineChannelInfo()
        #result = refineChannelInfo.retrieveInfo(request.args.get("query"), )
        #result = '{"video_id": "None"}' 
        #dict1 = json.loads(result)

        #print(dict1)
        #return dict1

api.add_resource(RetrieveChannelInfo, '/youtube/channelList')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


