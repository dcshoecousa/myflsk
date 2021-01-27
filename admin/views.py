"""
author: gd199
date: 2021-01-10

"""
from flask import views, session, request
# from common.RedisHelper import redis_conn
from common.SignalHelper import audit_logging
from common.MysqlHelper import db
from sqlalchemy import and_, or_


class Login(views.MethodView):
    methods = ['GET']

    def get(self):
        return '1'


class Users(views.MethodView):
    methods = ['GET', 'POST']

    def get(self, *args, **kwargs):
        pass

    def post(self):
        pass