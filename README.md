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


`celery -A tasks worker --loglevel=info  --app=proj -Q queue_add,queue_div,queue_log,queue_modf`

if add the `-Q` arguement, celery will start queues that you specify.In above example is `queue_add,queue_div,queue_log,queue_modf`
, so if you put same other task to default, it will not be invoked.