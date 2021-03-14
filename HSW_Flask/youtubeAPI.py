import pandas as pd
from youtube_api import YouTubeDataAPI

from flask import Flask
from flask import render_template, make_response
from flask import request

class RefineChannelInfo: 
    def __init__(self):
	    #print(apiKey)
        print("init")

    def mainPage(self):
        headers = {'Content-Type':"text/html"}
        return make_response(render_template('home.html'),200,headers)