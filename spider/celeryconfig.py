#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:23

from kombu import Queue
from kombu import Exchange
from celery.schedules import crontab,timedelta
from datetime import datetime
BROKER_URL='pyamqp://favoruser:favormylikes@192.168.3.2:5672//'
CELERY_RESULT_BACKEND = 'amqp://favoruser:favormylikes@192.168.3.2:5672//'
CELERY_TIMEZONE='Asia/Shanghai'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'spider.tasks'
)

#过期时间
CELERY_TASK_RESULT_EXPIRES=3600

