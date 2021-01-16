"""
author: gd199
date: 2021-01-10

"""
from flask import request
from flask_restful import Resource
from models.user import User as UserModel
from common.Serializer import Serializer
from common.MysqlHelper import db

class User(Resource):
    methods = ['POST', 'GET']

    def post(self):
        user = Serializer(UserModel).instance
        user.save()
        user_serializer = Serializer(instance=user)
        return user_serializer.data, 201

    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if user is None:
            return None, 404
        user_serializer = Serializer(instance=user)
        status_code = 200 if user else 404
        return user_serializer.data, status_code

class Login(Resource):
    methods = ["GET"]

    def get(self):
        return {'Test': 'Test'}, 200
