import datetime
import sqlalchemy.types as types


class MyDateTime(types.TypeDecorator):
    impl = types.DateTime
    
    def process_bind_param(self, value, dialect):
        if type(value) is str:
            return datetime.datetime.strptime(value, '%Y-%m-%d')
        return value