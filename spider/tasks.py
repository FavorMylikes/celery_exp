#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:23

from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from celery import group
from spider import app
from datetime import datetime
from lxml import etree
from spider.items import TopicItem
import requests,math
logger = get_task_logger(__name__)

@app.task
def fresh():
    def _fresh():
        url = "https://www.douban.com/group/beijingzufang/discussion"
        url += "?start=0"
        content = requests.get(url, proxies={'http': 'socks5://127.0.0.1:1080'}).content
        tree = etree.HTML(content)
        for tr in tree.xpath('//*[@id="content"]/div/div[1]/div[2]/table/tr')[2:]:
            item = TopicItem()
            item["title"] = tr.xpath("td[1]/a")[0].attrib["title"]
            item["url"] = tr.xpath("td[1]/a")[0].attrib["href"]
            item["author"] = tr.xpath("td[2]/a/text()")[0].strip()
            item["comment_count"] = (tr.xpath("td[3]/text()") + ["0"])[0].strip()
            item["lasttime"] = tr.xpath("td[4]/text()")[0].strip()
            if len(item["lasttime"]) == 11:
                item["lasttime"] = str(datetime.now().year) + '-' + item["lasttime"]
            logger.debug(item["url"])
            yield save_topic.s(item)
    group(_fresh())()
        # save_topic.delay(item)
        # yield Request(item["url"], callback=self.topic_detail_handler, meta={"topicItem": item})

@app.task
def save_topic(topic_item):
    logger.info(topic_item)

if __name__ == '__main__':
    # app.worker_main(argv="--loglevel=info  --app=spider --hostname=001@%h  -Q fresh,save_topic,default --schedule=spider/celrybeat-schedule".split(" "))
    argv="tasks worker " \
         "--beat " \
         "--loglevel=info " \
         "--app=spider " \
         "--hostname=001@%h " \
         "--queues fresh,save_topic,default " \
         "--schedule=celrybeat-schedule".split(" ")
    app.start(argv=argv)