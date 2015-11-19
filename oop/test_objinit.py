# -*- coding: utf8 -*-


class MyClass:

    def __new__(cls, *args, **kwargs):
        print("inside MyClass.__new__()")
        return super(MyClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("inside MyClass.__init__()")

    def __call__(self, *args, **kwargs):
        print("inside MyClass.__call__()")

print("defind class MyClass finished")
print("-" * 50)
x = MyClass()
print("-" * 50)
x()
