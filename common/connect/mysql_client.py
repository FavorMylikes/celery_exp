#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-7-12 下午5:14
import pymysql
# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

__all__=['sqlalchemy_url','conn_mysql','session_mysql']
mysql_config={"host":'192.168.3.2',"port":3306,"user":"douban","passwd":'favormylikes',"db":"douban","charset":"utf8mb4"}
sqlalchemy_url='mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}'.format(**mysql_config)

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