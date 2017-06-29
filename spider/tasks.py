#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:23

from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from demo import app
from datetime import datetime
from lxml import etree
import requests

import math

@app.task
def fresh():
    url="https://www.douban.com/group/beijingzufang/discussion"
    content=requests.get(url, proxies={'http': 'socks5://127.0.0.1:1080'}).content
    tree=etree.HTML(content)
    for tr in tree.xpath('//*[@id="content"]/div/div[1]/div[2]/table/tr')[2:]:
        item = topicItem()
        item["title"] = tr.xpath("td[1]/a")[0].root.attrib["title"]
        item["url"] = tr.xpath("td[1]/a")[0].root.attrib["href"]
        item["author"] = tr.xpath("td[2]/a/text()").extract()[0].strip()
        item["comment_count"] = (tr.xpath("td[3]/text()").extract() + ["0"])[0].strip()
        item["lasttime"] = tr.xpath("td[4]/text()").extract()[0].strip()
        if len(item["lasttime"]) == 11:
            item["lasttime"] = str(datetime.now().year) + '-' + item["lasttime"]
        logger.debug(item["url"])
        yield Request(item["url"], callback=self.topic_detail_handler, meta={"topicItem": item})