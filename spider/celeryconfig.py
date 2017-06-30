#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:23

from kombu import Queue
from kombu import Exchange
from celery.schedules import crontab,timedelta
from datetime import datetime
BROKER_URL='pyamqp://favoruser:favormylikes@192.168.3.2:5672//'
# The AMQP result backend is scheduled for deprecation in
# version 4.0 and removal in version v5.0.
# Please use RPC backend or a persistent backend.
# CELERY_RESULT_BACKEND = 'amqp://favoruser:favormylikes@192.168.3.2:5672//'
CELERY_RESULT_BACKEND = 'rpc://'

CELERY_TIMEZONE='Asia/Shanghai'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'spider.tasks'
)

#过期时间
CELERY_TASK_RESULT_EXPIRES=3600
#默认队列
CELERY_DEFAULT_QUEUE = "default"

CELERY_ROUTES={'spider.tasks.fresh': {'queue': 'fresh'},
               'spider.tasks.save_topic': {'queue': 'save_topic'},}

CELERY_QUEUES = (
    Queue('fresh',routing_key="fresh"),
    Queue('save_topic',routing_key="save_topic"),
    Queue('default'),
)

CELERYBEAT_SCHEDULE = {
    'send-email-every-5-minute': {    # 定时任务的名字
        'task': 'spider.tasks.fresh',     # 具体对应的Task
        'schedule':  timedelta(seconds=50),# 定时设置，这里表示30s执行一次
        # 'args': (datetime.now().strftime("%x %X"),) ,
    }
}