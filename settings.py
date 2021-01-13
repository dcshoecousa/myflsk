"""
author: gd199
date: 2021-01-10

"""


class Settings:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Wgd,492261648@192.168.1.104:3307/flk?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1


class DevSettings(Settings):
    DEBUG = True
    SECRET_KEY = 'THIS_IS_DEV_SECURE_KEY'


class ProductionSettings(Settings):
    DEBUG = False
    SECRET_KEY = 'THIS_IS_PRODUCTION_SECURE_KEY'
