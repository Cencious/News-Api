import os

class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey=bc65644257bd47a4acce597b88496581'
    ALL_NEWS_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=bc65644257bd47a4acce597b88496581'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}