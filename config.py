import os
class Config:
    '''
    Parent configuration class
    '''
    API_SOURCES_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    

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
   