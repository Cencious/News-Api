from flask import render_template
from . import main
from ..requests import get_sources, get_articles
from ..models_sources import Source


# views
@main.route('/') # route decorator defining the view function
def index():
    """
   view root page function that returns the index the page and its data
    """
    # Getting the popular categories
    general = get_sources('general')
    sports = get_sources('sports')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    science = get_sources('science')


    title = 'Welcome to Cedi News Hub '

    return render_template('index.html', title=title, general=general, sports=sports, business=business, technology=technology, entertainment=entertainment, science=science) #template name vs view name

@main.route('/<source_id>')
def articles(source_id):
    """
    Articles page
    """
    news_source = get_articles(source_id)
    title = f'Welcome to {source_id}'
    return render_template('news.html', title=title, name = source_id, news = news_source)