"""
author: gd199
date: 2021-01-10

"""

from api import rest_api
from api.views import User, UserProfile

rest_api.add_resource(User, '/users/<int:id>', '/users')
rest_api.add_resource(UserProfile, '/profiles/<int:userId>')

