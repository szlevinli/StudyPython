# -*- coding: utf8 -*-


class MyMetaClass(type):

    def __call__(cls, *args, **kwargs):
        print("inside MyMetaClass.__call__()")

    def __new__(cls, className, superClasses, attributeDict):
        print("className: ", className)
        print("superClasses: ", superClasses)
        print("attributeDict: ", attributeDict)
        return type.__new__(cls, className, superClasses, attributeDict)

    def __init__(cls, className, superClasses, attributeDict):
        print("inside MyMetaClass.__init__()")


class S(object, metaclass=MyMetaClass):
    print("inside class S")
    def __init__(self):
        print("inside S.__init__()")


class A(S, metaclass=MyMetaClass):
    print("inside class A")

print("start...")
s = S()