#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-7-3 上午10:32

from celery.loaders.base import BaseLoader
import logging
from sys import stderr
logger=logging.getLogger(__name__)
handler=logging.StreamHandler(stderr)
handler.setFormatter("")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class ProxyLoader(BaseLoader):
    """为每个worker设置一个专用的代理池"""
    count=0
    def on_worker_init(self):
        logger.info("ProxyLoader%s"%ProxyLoader.count)
        ProxyLoader.count+=1

