# from proj.tasks import inc
from proj.tasks import add
import time
for i in range(100):
    res=add.signature((i,1),queue='queue_add').delay()
    time.sleep(1)