"""
author: gd199
date: 2021-01-10

"""

from . import api
from api.views import Login

api.add_url_rule('/login', view_func=Login.as_view(name='login'))
