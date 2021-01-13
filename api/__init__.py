"""
author: gd199
date: 2021-01-10

"""

from flask import Blueprint

api = Blueprint('api', __name__)

from api.urls import *
