#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-7-12 上午11:27

import redis
redis_config={"host":'120.27.96.175',"port":8379,"password":'favormylikes'}
def conn_redis():
    return redis.StrictRedis(**redis_config)