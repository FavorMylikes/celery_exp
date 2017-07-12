Celery Demo
===================
### rabbitmqadmin usage
    
    -u \<username> -p \<passwrod>
or you can use long arguements like

    --username=guest --password=guest
user guest is for default so you can omit it
    
* delete all queue from rabbitmq
    
`rabbitmqadmin -u user -p pass list queues | awk '{print $2}'| xargs -n1 -I@ ./rabbitmqadmin -u user -p pass delete queue name=@`

* clear all queue from rabbitmq

`rabbitmqadmin -u user -p pass list queues | awk '{print $2}'| xargs -n1 -I@ ./rabbitmqadmin -u user -p pass purge queue name=@`

### worker start args


`celery -A tasks worker --loglevel=info  --app=demo -Q queue_add,queue_div,queue_log,queue_modf`

if add the `-Q` arguement, celery will start queues that you specify.In above example is `queue_add,queue_div,queue_log,queue_modf`
, so if you put same other task to default, it will not be invoked.

`celery -B -A tasks worker --loglevel=info  --app=spider --hostname=001@%h  -Q fresh,save_topic,default --schedule=spider/celrybeat-schedule
`

start with beat schedule

if this message `warning: Debugger speedups using cython not found`  show up begin of console,maybe you need run below command to build

`"/usr/bin/python3.5" "/home/mylikes/Downloads/pycharm-2017.1.3/helpers/pydev/setup_cython.py" build_ext --inplace`

