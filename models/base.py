from sqlalchemy import Column, String, Integer, DateTime
from common.MysqlHelper import db
import datetime

class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key = True)
    version = Column(Integer, default = 1)
    create_on = Column(DateTime, default = datetime.datetime.now)

    def __str__(self):
        return str(id)

    def save(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()
    
