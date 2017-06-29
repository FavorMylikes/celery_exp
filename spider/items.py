#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:41
from spider.base import Field,BaseItem

class topicItem(BaseItem):
    author = Field()
    content = Field()
    comment_count = Field()
    comment_id_count = Field()
    comment_time_var = Field()
    comment_distinct_count = Field()
    createtime = Field()
    releasetime = Field()
    lasttime = Field()
    url = Field()
    content_hash = Field()
    key = Field()
if __name__ == '__main__':
    print(topicItem())