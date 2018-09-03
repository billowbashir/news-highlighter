# import the app instance_
from app import app
#  urllib.request module that will help us create a connection to our API URL and send a request
#  json modules will format the JSON response to a Python dictionary.
import urllib.request,json

from .models import source
Source = source.Source

# get the api key
api_key=app.config['KEY']

# get the base url
base_url_source=app.config['BASE_URL_SOURCE']
# base_url_articles
base_url_articles=app.config['BASE_URL_ARTICLES']


def get_source():
    '''
    Function that gets the json response to our url request
    '''

    # store the formatted url in get_source_url, send the request, read the response with url....
    # ...read and then store it in get_source_data then convert it to python dictionary using json.loads
    get_source_url = base_url_source.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results


def process_results(source_list):

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        source_object = Source(id,name)
        source_results.append(source_object)
    return source_results
def get_articles():
    '''
    Function that gets the json response to our url request
    '''

    # store the formatted url in get_source_url, send the request, read the response with url....
    # ...read and then store it in get_source_data then convert it to python dictionary using json.loads
    get_article_url = base_url_articles.format(api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_art_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)


    return articles_results


def process_article_results(articles_list):

    articles_results = []
    for article_item in articles_list:
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        urlToImage=article_item.get('urlToImage')
        publishedAt=article_item.get('publishedAt')

        articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
        articles_results.append(articles_object)
    return articles_results
