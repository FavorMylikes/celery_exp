#-*-coding:utf-8-*-
# @desc Created by FavorTGD.
# @author : FavorMylikes<l786112323@gmail.com>
# @since : 17-6-29 下午7:51

# incomplete
class Field():
    pass

class BaseItem(dict):

    def __new__(cls):
        fields = {}
        for v in dir(cls):
            if isinstance(v,Field):
                fields[v]=""
        return dict(**fields)
