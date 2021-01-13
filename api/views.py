"""
author: gd199
date: 2021-01-10

"""

from flask import views


class Login(views.MethodView):
    methods = ["GET"]

    def get(self):
        return 'Api.Login'
