from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import render_template, make_response

from youtubeAPI import RefineChannelInfo
import numpy as np

app = Flask(__name__)
api = Api(app)

apiKey = ''
q = ''

""" Home Directory
	
	root Dir 접속 라우터

	Args : Empty
	Return : Empty
"""
@app.route('/')
def hello_world():
	return 'Youtube 댓글 분석기 그 위대한 시작...'


""" RefineChannelInfo
    
    Youtube Api Channel Response 정제 Class

""" 
class RetrieveChannelInfo(Resource):
    def get(self):
        hearders = {'Content-Type':'text/html'}

        refineChannelInfo = RefineChannelInfo()
        result_search = refineChannelInfo.retrieveInfo(q, apiKey)
        print(result_search)

        if len(result_search) > 0:
            result = result_search[0]
            return make_response(render_template('table.html',data = result),200,hearders)

        return make_response(render_template('home.html'),200,hearders)         

api.add_resource(RetrieveChannelInfo, '/youtube/channelList')


if __name__ == '__main__':

    apiKey = input("API KEY를 입력하세요 :: ")
    q = input("검색할 키워드를 입력하세요 :: ")

    app.run(host="0.0.0.0", port=5000)


