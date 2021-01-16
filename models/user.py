"""
author: gd199
date: 2021-01-11

"""

from sqlalchemy import Column, String, Enum, Integer
from models.base import Base


class User(Base):
    """
    User Table
    """
    __tablename__ = 'flk_user'
    name = Column(String(32), unique=True, nullable=False)
    password = Column(String(256), nullable = False)
    user_profile_id = Column(Integer, unique=True, nullable=True)

    

class UserProfile(Base):
    """
    User Profile Table
    """

    __tablename__ = 'flk_userprofile'
    email = Column(String(64), unique=True, nullable=True)
    gender = Column(Enum('男', '女'), default='男')

