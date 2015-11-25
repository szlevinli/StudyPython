# -*- coding: utf8 -*-


class MyMetaClass(type):
    print("inside class MyMetaClass")

    def __call__(cls, *args, **kwargs):
        print("inside MyMetaClass.__call__()")

    def __new__(cls, className, superClasses, attributeDict):
        print("inside MyMetaClass.__call__()")
        # print("className: ", className)
        # print("superClasses: ", superClasses)
        # print("attributeDict: ", attributeDict)
        return type.__new__(cls, className, superClasses, attributeDict)

    def __init__(cls, className, superClasses, attributeDict):
        print("inside MyMetaClass.__init__()")


class S(object, metaclass=MyMetaClass):
    print("inside class S")

    def __init__(self):
        print("inside S.__init__()")


class A:
    print("inside class A")

    def __init__(self):
        print("inside A.__init__()")


class B(S):
    print("inside class B")

    def __init__(self):
        print("inside B.__init__()")

print("start...")
s = S()
a = A()
b = B()
