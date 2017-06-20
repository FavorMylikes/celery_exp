#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/6/19 23:49
from __future__ import absolute_import, unicode_literals
from celery import Celery

# app = Celery('tasks',
#              broker='pyamqp://guest:favormylikes@192.168.3.2:5672//',
#              backend='rpc://',
#              include=['proj.tasks']
#              )
app = Celery('proj',
             broker='pyamqp://favoruser:favormylikes@localhost:5672//',
             backend = 'rpc://',
             include=['proj.tasks'],
             )
app.conf.update(
    result_expires=3600,
)

@app.task
def add(x, y):
    return x+y

@app.task
def inc(x):
    x+=1
    if x<10:
        inc.delay(x)
        return x
    else:
        return x
if __name__ == '__main__':
    #--pool could be 'eventlet' or 'gevent'
    # multi restart w1 -A proj -l info
    # 'multi','start','3','--pool=gevent'
    #
    app.start(argv=['tasks','multi','start','w1','--loglevel=info'])