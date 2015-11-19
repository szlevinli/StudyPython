# -*- coding: utf8 -*-

class Singleton(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        print('111')
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance

class A(metaclass=Singleton):
    pass

a = A()