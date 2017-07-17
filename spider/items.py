#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:41
from common.base import Field,BaseItem,BaseModel
from sqlalchemy import Column, String, Integer,Text,Float,DateTime,BigInteger,ForeignKey
from sqlalchemy.dialects.mysql import DOUBLE
from datetime import datetime
class Topic(BaseModel):
    __tablename__ = 'topic'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    title = Column(String(length=255,collation='utf8mb4'),nullable=False)
    author_id = Column(Integer,ForeignKey('author.id'),nullable=False)
    content = Column(Text(collation='utf8mb4'),nullable=False)
    comment_count = Column(Integer)
    comment_id_count = Column(Integer)
    comment_time_var = Column(type_=DOUBLE)
    comment_distinct_count = Column(Integer)
    createtime = Column(DateTime,default=datetime.now(),nullable=False)
    releasetime = Column(DateTime,default=datetime.now(),nullable=False)
    lasttime =Column(DateTime,default=datetime.now(),nullable=False)
    url_params = Column(String(length=255),default='',nullable=False)
    content_hash = Column(BigInteger)
    def __init__(self):
        self.key=""

def MonitorPage(BaseModel):
    __table__='monitor_page'
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    url_templet = Column(String(length=255),nullable=False)
    lasttime=Column(DateTime,default=datetime.now())
    type=Column(String(length=20),nullable=False)

def Comment(BaseModel):
    __table__ = 'commment'
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    topic_id=Column(Integer,ForeignKey('topic.id'),nullable=False)
    comment=Column(String(length=255,collation='utf8mb4'),nullable=False)
    release_time = Column(DateTime,default=datetime.now(),nullable=False)
    author_id = Column(Integer,ForeignKey('author.id'),nullable=False)

def Author(BaseModel):
    __table__ = "author"
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    name = Column(String(length=255,collation='utf8mb4'),nullable=False)
    url_params = Column(String(length=255),nullable=False)

def Picture(BaseModel):
    __table__ ="picture"
    id = Column(Integer, primary_key=True, autoincrement=True,nullable=False)
    url_params = Column(String(length=255),nullable=False)
    topic_id = Column(Integer,ForeignKey('topic.id'),nullable=False)

if __name__ == '__main__':
    from common.connect.mysql_client import session_mysql
    from sqlalchemy.orm import sessionmaker
    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    session=session_mysql()
    topic=Topic()
    topic.title="title"
    topic.author="author"
    topic.content="content"
    string = topic.serialize()
    top = Topic.deserialize(string)
    print(top)
    # session.add(topic)
    # session.commit()
