#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-7-12 下午5:14
import pymysql
mysql_config={"host":'127.0.0.1',"port":3306,"user":"root","passwd":'',"db":"douban_group","charset":"utf8mb4"}
def conn_mysql():
    return pymysql.connect(**mysql_config)