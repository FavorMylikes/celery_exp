BROKER_URL='pyamqp://favoruser:favormylikes@localhost:5672//'
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_TIMEZONE='Asia/Shanghai'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'proj.tasks'
)

