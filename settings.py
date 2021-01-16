"""
author: gd199
date: 2021-01-10

"""


class Settings:
    SQLALCHEMY_DATABASE_URI = "sqlite:///flk.db"


class DevSettings(Settings):
    DEBUG = True
    SECRET_KEY = 'THIS_IS_DEV_SECURE_KEY'


class ProductionSettings(Settings):
    DEBUG = False
    SECRET_KEY = 'THIS_IS_PRODUCTION_SECURE_KEY'
