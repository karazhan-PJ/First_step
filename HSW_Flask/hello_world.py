from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import render_template, make_response

from youtubeAPI import RefineChannelInfo

app = Flask(__name__)
api = Api(app)

apiKey = ''

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
	    #refineChannelInfo = RefineChannelInfo()

        headers = {'Content-Type':"text/html"}
        return make_response(render_template('table.html'),200,headers)


api.add_resource(RetrieveChannelInfo, '/youtube/channelList')
	
if __name__ == '__main__':
    #apiKey = input("API KEY를 입력하세요 :: ")
    app.run(host="0.0.0.0", port=5000, debug=True)


