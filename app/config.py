class Config(object):
    pass

class DevelpomentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True

class ProductionConfig(Config):
    DEBUG=False

app_config = {
    'development' : DevelpomentConfig,
    'production' : ProductionConfig
}    