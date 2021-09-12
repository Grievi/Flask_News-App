from flask import Flask, render_template
from newsapi import NewsApiClient
import newsapi

app = Flask(__name__,template_folder='templates')

@app.route('/')
def Index():
    newsapi = NewsApiClient
    (api_key="b0f75ce660c0466a9a98c2478f8abb62")
    
 