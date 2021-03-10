from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import make_response


app = Flask(__name__)
api = Api(app)

class HttpSimilarIntent(Resource):
    def get(self):
	    return "hello"


@app.route('/')
def hello_world():

	return 'Hello World!'

api.add_resource(HttpSimilarIntent, '/youtube/channelList')
	
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)


