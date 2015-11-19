# -*- coding: utf8 -*-


class MyMetaClass(type):

    def __new__(cls, className, superClasses, attributeDict):
        print("className: ", className)
        print("superClasses: ", superClasses)
        print("attributeDict: ", attributeDict)
        return type.__new__(cls, className, superClasses, attributeDict)


class S(object, metaclass=MyMetaClass):
    print("inside class S")


class A(S, metaclass=MyMetaClass):
    print("inside class A")
