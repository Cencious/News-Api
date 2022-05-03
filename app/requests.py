import urllib.request, json  # urllib.request will help us create a connection to the API URL and send a request.
from .models_sources import Source
from .models_articles import Articles
from datetime import datetime


# Getting the api key
api_key = None

# Getting the news base url
base_url = None

# Getting the articles
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ALL_NEWS_BASE_URL']

def get_sources(category):
    """
    Function that gets the json response to the url request
    """
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response["sources"]:
            source_results_list = get_sources_response["sources"]
            source_results = process_sources(source_results_list)

    return source_results

def process_sources(sources_list):
    """
    function that processes the json and returns a list of objects
    Args:
        source_list: a list of dictionaries that contain source details
    Returns:
        sources_results: a list of source objects
    """
    source_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        if url:
            source_object = Source(id, name, description, url, category, language, country)
            source_results.append(source_object)

    return source_results


def get_articles(source_id):
    '''
    Function that gets articles based on the source id
    '''
    get_article_url = articles_url.format(source_id, api_key)

    with urllib.request.urlopen(get_article_url) as url:
        articles_info = url.read()
        articles_response = json.loads(articles_info)

        articles_results = None

        if articles_response['articles']:
            articles_results = process_articles(articles_response['articles'])

    return articles_results


def process_articles(my_articles):
    '''
    Function that processes the json results for the articles
    '''
    articles_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]), month=int(date_published[5:7]),
                               day=int(date_published[8:10]), hour=int(date_published[11:13]),
                               minute=int(date_published[14:16]))

        if urlToImage:
            article_source_object = Articles(author, title, description, url, urlToImage, publishedAt)
            articles_list.append(article_source_object)

    return articles_list

def search_articles(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=NEWS_API_KEY'.format(api_key,article_name)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['results']:
            search_article_list = search_article_response['results']
            search_article_results = process_sources(search_article_list)


    return search_article_results
