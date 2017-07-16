#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:51

from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
BaseModel = declarative_base()
class Field():
    pass

class BaseItem(dict):

    def __new__(cls):
        fields = {}
        for n in dir(cls):
            v = getattr(cls, n)
            if isinstance(v,Field):
                fields[n]=""
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