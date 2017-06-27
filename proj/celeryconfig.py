BROKER_URL='pyamqp://favoruser:favormylikes@localhost:5672//'

##NotImplementedError: The "rpc" result backend does not support chords!
#CELERY_RESULT_BACKEND = 'rpc://'#using rpc for backend result
CELERY_RESULT_BACKEND = 'amqp://favoruser:favormylikes@localhost:5672//'
CELERY_TIMEZONE='Asia/Shanghai'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'proj.tasks'
)
#路由配置，对应的任务会被push到对应的队列中，同时，任务也只接受对应的任务消息，不会接受到其他队列的消息
CELERY_ROUTES={'proj.tasks.add': {'queue': 'queue_add'},
          'proj.tasks.div': {'queue': 'queue_div'},
          'proj.tasks.log': {'queue': 'queue_log'},
          'proj.tasks.modf': {'queue': 'queue_modf'},
          'proj.tasks.inc': {'queue': 'queue_inc'}}
#过期时间
CELERY_TASK_RESULT_EXPIRES=3600