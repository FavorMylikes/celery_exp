#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-7-12 下午5:14
import pymysql
# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

__all__=['BaseModel','sqlalchemy_url','conn_mysql','session_mysql']
# 创建对象的基类:
Base = declarative_base()
mysql_config={"host":'192.168.3.2',"port":3306,"user":"douban","passwd":'favormylikes',"db":"douban","charset":"utf8mb4"}
sqlalchemy_url='mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}'.format(**mysql_config)
class BaseModel(Base):
    def as_dict(self):
        return dict((column.name ,str(getattr(self, column.name))) for column in self.__table__.columns)
def conn_mysql():
    return pymysql.connect(**mysql_config)

def session_mysql():
    """
    :rtype: Session
    """
    # 初始化数据库连接:
    engine = create_engine(sqlalchemy_url)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    return DBSession()

if __name__ == '__main__':
    # 定义User对象:
    class User(Base):
        # 表的名字:
        __tablename__ = 'test'

        # 表的结构:
        id = Column(Integer, primary_key=True,autoincrement=True)
        user = Column(String(20),default="hh")


    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)



    user=User()
    session=session_mysql()
    print(type(session))
    session.add(user)
    session.commit()
    print(user.id)
    user=session.query(User).filter(User.id == '5').one()
    print("{0.id},{0.user}".format(user))
