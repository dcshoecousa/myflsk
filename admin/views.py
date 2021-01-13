"""
author: gd199
date: 2021-01-10

"""
from flask import views, session, request
from common.RedisHelper import redis_conn
from common.SignalHelper import audit_logging
from common.MysqlHelper import db
from admin.models import User, UserProfile
import json
from sqlalchemy import and_, or_


class Login(views.MethodView):
    methods = ['GET']

    def get(self):
        audit_logging.send()
        session['dc'] = 'dc'
        redis_conn.setex('xxx', 30, 'xxxx')
        return 'Admin.Login'


class Users(views.MethodView):
    methods = ['GET', 'POST']

    def get(self, *args, **kwargs):
        ret = db.query(User).all()
        return json.dumps(ret)

    def post(self):
        data = request.data
        if data:
            data_json = json.loads(request.data)
            if data_json:
                name = data_json.get('name')
                if not name:
                    return "errors"

                user = User(name=name)
                user_profile = UserProfile(age=30)
                user.user_profile = user_profile
                db.add(user)
                db.commit()
                return 'success'
        return 'failure'