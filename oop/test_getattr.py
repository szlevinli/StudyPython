# -*- coding: utf8 -*-


class OnlyOne:

    def __init__(self):
        self.a = 'a'

    def __getattr__(self, name):
        print("%s attribute is not exists!" % name)


x = OnlyOne()
a = x.a
b = x.b
print(a)
print(b)
