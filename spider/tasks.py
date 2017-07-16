#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:23

from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from celery import group,chain
from spider import app
from datetime import datetime
from lxml import etree
from spider.items import Topic
from common.connect.redis_client import conn_redis
import requests,math

logger = get_task_logger(__name__)
r_cli=conn_redis()

@app.task
def fresh():
    # def _fresh():
    #     url = "https://www.douban.com/group/beijingzufang/discussion"
    #     url += "?start=0"
    #     content = requests.get(url, proxies={'http': 'socks5://127.0.0.1:1080'}).content
    #     tree = etree.HTML(content)
    #     for tr in tree.xpath('//*[@id="content"]/div/div[1]/div[2]/table/tr')[2:]:
    #         item = TopicItem()
    #         item["title"] = tr.xpath("td[1]/a")[0].attrib["title"]
    #         item["url"] = tr.xpath("td[1]/a")[0].attrib["href"]
    #         item["author"] = tr.xpath("td[2]/a/text()")[0].strip()
    #         item["comment_count"] = (tr.xpath("td[3]/text()") + ["0"])[0].strip()
    #         item["lasttime"] = tr.xpath("td[4]/text()")[0].strip()
    #         if len(item["lasttime"]) == 11:
    #             item["lasttime"] = str(datetime.now().year) + '-' + item["lasttime"]
    #         logger.debug(item["url"])
    #         yield save_topic.s(item)
    # group(_fresh())()
    url = "https://www.douban.com/group/beijingzufang/discussion"
    url += "?start=0"
    chain(get_proxy.s()|get_content.s(url)|list_handler.s())()

        # save_topic.delay(item)
        # yield Request(item["url"], callback=self.topic_detail_handler, meta={"topicItem": item})


@app.task
def get_content(proxy,url):
    return requests.get(url, proxies={'http': proxy}).content.decode()


@app.task
def get_proxy():
    global r_cli
    return r_cli.rpoplpush("proxy_queue","proxy_queue").decode()

@app.task
def list_handler(content):
    sign=[]
    tree = etree.HTML(content.encode())
    for tr in tree.xpath('//*[@id="content"]/div/div[1]/div[2]/table/tr')[2:]:
        item = Topic()
        item.title = tr.xpath("td[1]/a")[0].attrib["title"]
        item.url = tr.xpath("td[1]/a")[0].attrib["href"]
        item.author = tr.xpath("td[2]/a/text()")[0].strip()
        item.comment_count = (tr.xpath("td[3]/text()") + ["0"])[0].strip()
        item.lasttime = tr.xpath("td[4]/text()")[0].strip()
        if len(item["lasttime"]) == 11:
            item["lasttime"] = str(datetime.now().year) + '-' + item["lasttime"]
        logger.debug(item["url"])
        sign.append(item)
    group(*sign)()


@app.task
def save_topic(topic_item):
    logger.info(topic_item)


def main():
    from sys import path
    from os.path import join,dirname
    path.append(join(dirname(__file__), '..'))
    print("worker starting ")
    argv = "tasks worker " \
           "--beat " \
           "--loglevel=info " \
           "--logfile=spider/log/%n%I.log "\
           "--app=spider " \
           "--hostname=001@%h " \
           "--queues fresh,save_topic,get_proxy,list_handler,get_content " \
           "--schedule=celrybeat-schedule".split(" ")
    app.start(argv=argv)
    print("worker started")

if __name__ == '__main__':
    # app.worker_main(argv="--loglevel=info  --app=spider --hostname=001@%h  -Q fresh,save_topic,default --schedule=spider/celrybeat-schedule".split(" "))
    main()