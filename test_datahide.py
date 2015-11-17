# -*- coding: utf8 -*-


class DataHide():

    """变量前加两个__可以实现隐藏
    实际上python会将有前缀两个下划线的变量进行“名称改编”(name mangling)
    改编后的名字为_className__variableName
    """
    __v = 0  # 将进行name mangling, _DataHide__v
    v = 1

    def __init__(self):
        self.s = 'sss'
        self.__s = '__s'  # 将进行name mangling, _DataHide__s

d = DataHide()

print(DataHide.v)
print(DataHide._DataHide__v)
print(d.s)
print(d._DataHide__s)
# print(d.__s)
# print error AttributeError: 'DataHide' object has no attribute '__s'
# print(DataHide.__v)
# print error AttributeError: 'DataHide' object has no attribute '__v'
