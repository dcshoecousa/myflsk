"""
author: gd199
date: 2021-01-10

"""

from api import rest_api
from api.views import Login, User

rest_api.add_resource(Login, '/login')
rest_api.add_resource(User, '/user', '/user/<int:id>')

