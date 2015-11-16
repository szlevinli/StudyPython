# -*- coding: utf8 -*-

class DataHide():
    """变量前加两个__可以实现隐藏
    """
    __v = 0
    v = 0

d = DataHide()

print(DataHide.v)
print(DataHide.__v)
