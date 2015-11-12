# -*- coding: utf8 -*-


class ClsWith():

    '''演示 `with statement` 的实现原理
    用于with statement中的类必须实现__enter__()和__exit__()方法
    `with statement`最重要的作用就是实现资源的有效释放
    `with open() as file`就是典型的用法，无需关闭文件`with statement`会处理
    使用这个语句处理创建数据库连接也非常有效
    '''

    def __enter__(self):
        print('is __entry__()')

    def __exit__(self, type, value, traceback):
        print('is __exit__()')

    def __init__(self):
        print('is __init__()')

if __name__ == '__main__':
    with ClsWith() as c:
        print('is in `with`')
