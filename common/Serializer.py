import datetime
from flask_restful import reqparse
from flask_sqlalchemy.model import Model
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.sqltypes import DateTime

class Serializer:
    
    def __init__(self, model = None, instance = None):
        self.__model = model
        self.__instance = instance
        self.__parser = None

    @property
    def data(self):
        if self.__instance is None:
            raise ValueError("Data is None.")
        serializer_data = self.get_serializer_data()
        return serializer_data

    @property
    def instance(self):
        if self.__model is None:
            raise ValueError("Model is None.") 

        self.__parser = reqparse.RequestParser()
        members = self.get_members(self.__model)
        for member in members:
            self.__parser.add_argument(member)
        return self.get_instance()

    def get_instance(self):
        obj = self.__model()
        data = self.__parser.parse_args()
        for key, val in data.items():
            if hasattr(obj, key) and val is not None:
                setattr(obj, key, val)
        return obj   

    def get_serializer_data(self):
        serializer_data = {}
        for key, val in self.__instance.__dict__.items():
            if isinstance(val, (int, float, str, bool)):
                serializer_data[key] = val
            elif isinstance(val, datetime.datetime):
                serializer_data[key] = str(val)
        return serializer_data

    def get_members(self, obj):
        if obj is None:
            raise ValueError("Please given model or instance.")
        
        members = []
        obj_items = vars(obj).items()
        for name, type in obj_items:
            if isinstance(type, InstrumentedAttribute):   
                members.append(name)
        return members
