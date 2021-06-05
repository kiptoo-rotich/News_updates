from app import app
import urllib.request,json
from .models import News


#Get api key/SOURCES
api_key = app.config['API_KEY']

#Get the base url
base_url = app.config["API_SOURCES_URL"]

def get_news(group):
    '''
    Function that will get format url
    '''
    get_news_url = base_url.format(group,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)
        
        results = None
        
        if get_response['articles']:
            results_list = get_response['articles']
            results = process_news(results_list)
    return results

def process_news(news_List):
    '''
    Function that transforms results to a list
    '''
    news_list=[]
    for item in news_List:
        id = item.get('id')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        content = item.get('content')
        news_object = News(id, title, description, url, urlToImage, publishedAt, content)
        news_list.append(news_object)
    return news_list