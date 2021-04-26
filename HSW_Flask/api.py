from flask import Flask,request,Response
from flask_restful import Resource, Api
from youtubeAPI import RefineChannelInfo
import numpy as np
import json

app = Flask(__name__)
api = Api(app)

class RetrieveChannelInfo(Resource):
    def get(self):

        query = request.values.getlist("query")
        print(query)

        refineChannelInfo = RefineChannelInfo()
        result = refineChannelInfo.retrieveInfo(query,"")
        dict1 = json.loads(result)
        
        resp = flask.Response()
        resp.headers["Access-Control-Allow-Origin"] = "*"
        resp.set_data(dict1)
        
        return resp

api.add_resource(RetrieveChannelInfo, '/youtube/channelList')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


