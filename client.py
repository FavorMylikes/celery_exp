# from proj.tasks import inc
from proj.tasks import add
import time
for i in range(100):
    res=add.delay(i,1)
    time.sleep(1)