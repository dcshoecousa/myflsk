"""
author: gd199
date: 2021-01-23

"""

from common.MysqlHelper import db
from sqlalchemy import Column, String, Integer, DateTime
import datetime


class AuditModel(db.Model):

    __tablename__ = 'flk_audit_user'

    id = Column(Integer, primary_key=True)
    action = Column(String, nullable=False)
    user = Column(Integer, nullable=False)
    Create_time = Column(DateTime, default=datetime.datetime.now)

