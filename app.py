from flask import Flask, render_template
from newsapi import NewsApiClient
import newsapi

app = Flask(__name__,template_folder='templates')

@app.route('/')
def Index():
    # init
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
    # top headlines
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
                                          
    all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    
    articles = top_headlines['articles']
    all = all_articles[articles]

 