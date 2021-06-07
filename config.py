import os
class Config:
    '''
    Parent configuration class
    '''
    API_SOURCES_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    SECRET_KEY = 'qwerty'

class ProdConfig(Config):
    '''
    Production configuration class
    
    Args:
        Config: The parent class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class
    Args:
        Config:The parent configuration class
    '''
    DEBUG = True
   
config_options = {
'development':DevConfig,
'production':ProdConfig
}