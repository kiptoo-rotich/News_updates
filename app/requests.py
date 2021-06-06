from app import app
import urllib.request,json
from .models import News, News_details


#Get api key/SOURCES
api_key = app.config['API_KEY']

#Get the base url
base_url = app.config["API_SOURCES_URL"]
api_url = app.config["API_URL"]

def get_news(sources):
    '''
    Function that will get format url
    '''
    get_news_url = base_url.format(sources, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)
        
        results = None
        
        if get_response['sources']:
            results_list = get_response['sources']
            results = process_news(results_list)
    return results

def process_news(news_List):
    '''
    Function that transforms results to a list
    '''
    news_list=[]
    for item in news_List:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')
        news_object = News(id, name, description, url, category)
        news_list.append(news_object)
    return news_list

def get_articles(articles):
    get_news_articles = api_url.format(articles, api_key)
    with urllib.request.urlopen(get_news_articles) as url:
        get_article_data = url.read()
        article_response = json.loads(get_article_data)
        
        if article_response['articles']:
            articles_list = article_response['articles']
            article_results = process_articles(articles_list)
    return article_results

def process_articles(articles_List):
    articles_list = []
    for article in articles_List:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        article_object = News_details(id,author,title, description,urlToImage,publishedAt, content)
        articles_list.append(article_object)
    return articles_list