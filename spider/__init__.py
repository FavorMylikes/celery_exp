#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:23

from celery import Celery
app = Celery('spider')                                # 创建 Celery 实例
app.config_from_object('spider.celeryconfig')   # 通过 Celery 实例加载配置模块

