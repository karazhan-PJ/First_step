from flask import Flask,request,make_response
from flask_restful import Resource, Api
from youtubeAPI import RefineChannelInfo
import numpy as np
import json

app = Flask(__name__)
api = Api(app)
apiKey = "AIzaSyA0xZ5whsLAcleAFmDSwjwSUBaqX607GMs"

class RetrieveChannelInfo(Resource):
    def get(self):

        # 쿼리 받아옴
        query = request.values.getlist("query")
        print(query)

        refineChannelInfo = RefineChannelInfo()
        dict1 = refineChannelInfo.retrieveInfo(query,apiKey)
        #dict1 = json.loads(result)
        
        # response 객체 생성 및 Header 세팅
        resp = make_response(dict1)
        resp.headers["Access-Control-Allow-Origin"] = "*"
        
        return resp

api.add_resource(RetrieveChannelInfo, '/youtube/channelList')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, use_reloader=False, debug=False)


