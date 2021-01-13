"""
author: gd199
date: 2021-01-10

"""


from flask import Blueprint

admin = Blueprint('admin', __name__)

from admin.urls import *
from common.SignalHelper import audit_logging
from common.MysqlHelper import db
