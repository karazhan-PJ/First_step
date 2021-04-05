from flask import Flask
from flask_restful import Resource, Api
from flask import request

from youtubeAPI import RefineChannelInfo
import numpy as np

app = Flask(__name__)
api = Api(app)

class RetrieveChannelInfo(Resource):
    def get(self):
        print("Connect Check")


api.add_resource(RetrieveChannelInfo, '/youtube/channelList')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


