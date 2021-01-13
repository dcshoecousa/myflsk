"""
author: gd199
date: 2021-01-11

"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from common.MysqlHelper import db


class User(db.Model):

    __tablename__ = 'flk_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    profile_id = Column(Integer, ForeignKey("flk_userprofile.id"), unique=True)

    user_profile = relationship('UserProfile', backref='up')


class UserProfile(db.Model):

    __tablename__ = 'flk_userprofile'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
