"""
author: gd199
date: 2021-01-10

"""

from flask import Blueprint
from flask_restful import Api

api = Blueprint('api', __name__)
rest_api = Api(api)

from api.urls import *
from models import user
