"""
author: gd199
date: 2021-01-10

"""
from flask_restful import Resource
from models.UserModel import UserModel, UserProfileModel
from common.Serializer import Serializer


class User(Resource):
    methods = ['POST', 'GET']

    def post(self):
        user = Serializer(UserModel).instance
        user.save()
        user_serializer = Serializer(instance=user)
        return user_serializer.data, 201

    def get(self, *args, **kwargs):
        users = UserModel.query.all()
        if users.count == 0:
            return None, 404
        users_serializer = [Serializer(instance=user).data for user in users]
        return users_serializer, 200

    def get(self, id):
        user = UserModel.query.filter_by(id=id)[-1]
        if user is None:
            return None, 404

        user_serializer = Serializer(instance=user).data
        user_profile = UserProfileModel.query.filter_by(id=user.user_profile_id)[-1]
        if user_profile:
            user_serializer['profile'] = Serializer(instance=user_profile).data

        status_code = 200 if user else 404
        return user_serializer, status_code


class UserProfile(Resource):
    methods = ['GET', 'POST', 'PATCH']

    def post(self, userId):
        user = UserModel.query.filter_by(id=userId)[-1]
        if not user:
            return "User not exist", 404

        user_profile = Serializer(model=UserProfileModel).instance
        user_profile.save()

        user.user_profile_id = user_profile.id
        user.save()

        return "Success", 201

    def patch(self, userId):
        pass



