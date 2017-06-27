#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 2017/6/19 23:02
from celery import Celery
app = Celery('proj')                                # 创建 Celery 实例
app.config_from_object('proj.celeryconfig')   # 通过 Celery 实例加载配置模块
#可以通过该方法更新配置，不过我想把这些主要配置都写在celeryconfig.py模块里
# app.conf.update(
#     result_expires=3600,
# )