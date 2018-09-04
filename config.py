import os
class Config:
    '''
    General configuration parent class
    '''
    BASE_URL_SOURCE='https://newsapi.org/v2/sources?apiKey={}'
    BASE_URL_ARTICLES='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    # 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    KEY=os.environ.get('KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
