#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/6/19 23:49
from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from proj import app
import math
# app = Celery('tasks',
#              broker='pyamqp://guest:favormylikes@192.168.3.2:5672//',
#              backend='rpc://',
#              include=['proj.tasks']
#              )

logger = get_task_logger(__name__)

#bind之后就可以使用self参数表示task自身
@app.task(bind=True)
def retry(self,x):
    logger.info("retries {0.retries}".format(self.request))
    if self.request.retries<3:
        # default_retry_delay=3*60 180s
        # max_retries = 3
        raise self.retry(countdown=0)

@app.task
def add(x, y):
    return x+y
#autoretry_for 发现异常自动retry,最大retry为5
@app.task(autoretry_for=(Exception,),
          retry_kwargs={'max_retries': 5})
def modf(x):
#@return (小数部分，整数部分)
    return math.modf(x)

@app.task
def div(data):
    x,y=data
    try:
        return x/y
    except ZeroDivisionError as e:
        return 0
    
@app.task
def log(x,base=math.e):
    return math.log(x,base)

#ignore_result设置为True时
# get的时候会导致阻塞，且永远不会继续，status_code将永远是pending
@app.task
def inc(x):
    x += 1
    if x<10:
        inc.delay(x)
        return x
    else:
        return x

#下面的任务是用来确定exchange的作用
@app.task(ignore_result=True)
def send_email(message):
    logger.info("Message sended:\n%s" % message)


@app.task(ignore_result=True)
def save_db(message):
    logger.info("Message save database:\n%s" % message)


@app.task(ignore_result=True)
def save_redis(message):
    logger.info("Message save redis:\n%s" % message)

if __name__ == '__main__':
    #--pool could be 'eventlet' or 'gevent'
    # multi restart w1 -A proj -l info
    # 'multi','start','3','--pool=gevent'
    #
    # app.start(argv=['tasks','multi','start','w2','--loglevel=info'])
    # app.start(argv=['tasks','multi','stop','w1','--loglevel=info'])
    # app.start(argv=['tasks', 'worker', '--loglevel=info'])
    # 打印配置
    print(app.conf.humanize(with_defaults=False, censored=True))