from kombu import Queue
from kombu import Exchange
BROKER_URL='pyamqp://favoruser:favormylikes@192.168.3.2:5672//'
##NotImplementedError: The "rpc" result backend does not support chords!
#CELERY_RESULT_BACKEND = 'rpc://'#using rpc for backend result
CELERY_RESULT_BACKEND = 'amqp://favoruser:favormylikes@192.168.3.2:5672//'
CELERY_TIMEZONE='Asia/Shanghai'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'proj.tasks'
)
#路由配置，对应的任务会被push到对应的队列中，同时，任务也只接受对应的任务消息，不会接受到其他队列的消息
CELERY_ROUTES={'proj.tasks.add': {'queue': 'queue_add'},
          'proj.tasks.div': {'queue': 'queue_div'},
          'proj.tasks.log': {'queue': 'queue_log'},
          'proj.tasks.modf': {'queue': 'queue_modf'},
          'proj.tasks.inc': {'queue': 'queue_inc'},

          'proj.tasks.send_email': {'exchange':"for_send","routing_key":"send.email"},
          'proj.tasks.save_db': {'exchange':"for_save","routing_key":"save.db"},
          'proj.tasks.save_redis': {'exchange':'for_save',"routing_key":"save.redis"}}
#默认队列
CELERY_DEFAULT_QUEUE = "default"

#过期时间
CELERY_TASK_RESULT_EXPIRES=3600

#Topic exchanges例子
#假设有这些routing_key的队列
#[usa.news, usa.weather, norway.news, norway.weather]
#*匹配一个单词
#*.news匹配[usa.news,norway.news]
##匹配多个单词,顺序问题可能要测依一下
#usa.#匹配[usa.news,usa.weather]


CELERY_QUEUES = (
    Queue('send_email',Exchange('send',type='topic'), routing_key='send.*'),
    Queue('save_db', Exchange('save',type='topic'), routing_key='save.#'),
    Queue('save_redis', Exchange('save',type='topic'), routing_key='save.#'),
)