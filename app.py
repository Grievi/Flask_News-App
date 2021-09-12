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
    a_articles = all_articles[articles]

    news = []
    desc = []
    img = []
    n_date = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        n_date.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

        toplist = zip(news, desc, img, n_date, url)

    all_news = []
    all_desc = []
    all_img = []
    all_n_date = []
    all_url = []

    for j in range(len(a_articles)):
        every_article = a_articles[j]

        all_news.append(every_article['title'])
        all_desc.append(every_article['description'])
        all_img.append(every_article['urlToImage'])
        all_n_date.append(every_article['publishedAt'])
        all_url.append(every_article['url'])

        all = zip(all_news, all_desc, all_img, all_n_date, all_url)

    return render_template('index.html', toplist = toplist, all = all)


if __name__ == "__main__":
    app.run(debug=True)



 