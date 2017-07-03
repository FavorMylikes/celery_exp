#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-7-3 上午10:32

from celery.loaders.base import BaseLoader
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
class ProxyLoader(BaseLoader):
    """为每个worker设置一个专用的代理池"""
    count=0
    def on_worker_init(self):
        logger.info("worker init with %s" % ProxyLoader.count)
        ProxyLoader.count+=1