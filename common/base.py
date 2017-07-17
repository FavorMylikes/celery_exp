# -*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:51

from sqlalchemy.ext.declarative import declarative_base as real_declarative_base
from sqlalchemy.ext.serializer import loads, dumps
from typing import TypeVar, Type
__all__ = ['BaseModel']
declarative_base = lambda cls: real_declarative_base(cls=cls)
T = TypeVar("T", bound='BaseModel')
# 为继承的子类添加一些有用的方法，不能使用继承自base是因为，继承类必须要有__table__的值
@declarative_base
class BaseModel(object):
    """
    为SQLAlchemy添加一些默认的属性和方法
    """
    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def tojson(self):
        return self.columnitems

    def as_dict(self):
        return dict((column.name, str(getattr(self, column.name))) for column in self.__table__.columns)

    def serialize(self) ->str:
        return dumps(self).decode()

    @classmethod
    def deserialize(cls: Type[T], string: str)-> T:
        return loads(string.encode())

class Field():
    pass


class BaseItem(dict):
    def __new__(cls):
        fields = {}
        for n in dir(cls):
            v = getattr(cls, n)
            if isinstance(v, Field):
                fields[n] = ""
        return dict(**fields)


if __name__ == '__main__':

    class TopicItem(BaseItem):
        title = Field()
        author = Field()
        content = Field()
        comment_count = Field()
        comment_id_count = Field()
        comment_time_var = Field()
        comment_distinct_count = Field()
        createtime = Field()
        releasetime = Field()
        lasttime = Field()
        url = Field()
        content_hash = Field()
        key = Field()
