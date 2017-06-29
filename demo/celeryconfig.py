from kombu import Queue
from kombu import Exchange
from celery.schedules import crontab,timedelta
from datetime import datetime
BROKER_URL='pyamqp://favoruser:favormylikes@192.168.3.2:5672//'
##NotImplementedError: The "rpc" result backend does not support chords!
#CELERY_RESULT_BACKEND = 'rpc://'#using rpc for backend result
CELERY_RESULT_BACKEND = 'amqp://favoruser:favormylikes@192.168.3.2:5672//'
CELERY_TIMEZONE='Asia/Shanghai'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'demo.tasks'
)
#路由配置，对应的任务会被push到对应的队列中，同时，任务也只接受对应的任务消息，不会接受到其他队列的消息
CELERY_ROUTES={'demo.tasks.add': {'queue': 'queue_add'},
          'demo.tasks.div': {'queue': 'queue_div'},
          'demo.tasks.log': {'queue': 'queue_log'},
          'demo.tasks.modf': {'queue': 'queue_modf'},
          'demo.tasks.inc': {'queue': 'queue_inc'},
          'demo.tasks.send_email': {'exchange':"send","routing_key":"send.email"},
          'demo.tasks.save_db': {'exchange':"save","routing_key":"save.db"},
          'demo.tasks.save_redis': {'exchange':'save',"routing_key":"save.redis"},
          'demo.tasks.tick': {'queue': 'time_task'},}
#默认队列
CELERY_DEFAULT_QUEUE = "default"

#过期时间
CELERY_TASK_RESULT_EXPIRES=3600

#Topic exchanges例子
#假设有这些routing_key的队列
#[usa.news, usa.weather, norway.news, norway.weather]
#*匹配一个
#*.news匹配[usa.news,norway.news]
##匹配多个单词,顺序问题可能要测依一下
#usa.#匹配[usa.news,usa.weather]


CELERY_QUEUES = (
    Queue('send_email',Exchange('send',type='topic'), routing_key='send.*'),
    Queue('save_db', Exchange('save',type='topic'), routing_key='save.#'),
    Queue('save_redis', Exchange('save',type='topic'), routing_key='save.#'),
    Queue('default'),#如果设置了default_queue，则必须在queues中添加默认队列，且启动时必须带有默认队列
    Queue('time_task'),
)

#定时任务配置，每两秒执行一次
#启动之后会生成celerybeat-schedule文件用于存储上一次执行的时间
#也可以通过-s参数指定
CELERYBEAT_SCHEDULE = {
    'send-email-every-minite': {    # 定时任务的名字
        'task': 'spider.tasks.tick',     # 具体对应的Task
        'schedule':  timedelta(seconds=2),# 定时设置，这里表示30s执行一次
        'args': (datetime.now().strftime("%x %X"),) ,
    }
}