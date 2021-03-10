from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import make_response


from youtubeAPI import RefineChannelInfo


app = Flask(__name__)
api = Api(app)

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

apiKey = ''
class RetrieveChannelInfo(Resource):
    def get(self):
	    RefineChannelInfo(apiKey)

	    return "hello"


api.add_resource(RetrieveChannelInfo, '/youtube/channelList')
	
if __name__ == '__main__':
    apiKey = input("API KEY를 입력하세요 :: ")
    app.run(host="0.0.0.0", port=5000, debug=True)


