"""
author: gd199
date: 2021-01-10

"""

from . import admin
from admin.views import Login, Users

admin.add_url_rule('/login', view_func=Login.as_view(name='login'))
admin.add_url_rule('/users', view_func=Users.as_view(name='users'))
