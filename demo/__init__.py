#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/6/19 23:02
from celery import Celery
app = Celery('demo',loader='common.loaders.app:ProxyLoader')                                # 创建 Celery 实例
app.config_from_object('demo.celeryconfig')   # 通过 Celery 实例加载配置模块

