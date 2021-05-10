from decouple import config

class Config():
    TIMEZONE = config('TIMEZONE', default='America/Sao_Paulo')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    '''Settings to development environment
    '''
    DEBUG = True
    SQLALCHEMY_ECHO = True

class Production(Config):
    '''Settings to development environment
    '''
    pass

    