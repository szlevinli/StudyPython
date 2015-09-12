# -*- coding: utf-8 -*-

'''study os moudle
'''

import os


def extCount(path):
    '''count number of files for each extension in the give path

    return dictionary {ext_name: sum, ...}
    '''

    e = {}

    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            ext = os.path.splitext(f)[1]
            if ext in e:
                e[ext] += 1
            else:
                e[ext] = 1
    return e


def lsFileStat(path):
    '''list all file in then given directory along with
    thire length and mtime'''

    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            l = os.stat(f).st_size
            mt = os.stat(f).st_mtime
            from datetime import datetime
            dt = datetime.fromtimestamp(mt)
            print('filename={} length={} mtime={}'.format(
                os.path.join(path, f),
                l,
                dt.isoformat(' ')))


def dirtree(path, depth=0):
    """
    按指定格式打印目录树

    path=目录
    depth=目录层级 主要用于递归调用是使用

    目录树格式
    foo
    |-- a.txt [file]
    |-- b.txt [file]
    |-- code
    |   |-- a.py [file]
    |   |-- b.py [file]
    |   |-- docs
    |   |   |-- a.txt [file]
    |   |   \-- b.txt [file]
    |   \-- x.py [file]
    |-- y.txt [file]
    \-- z
    """

    # 对目录list进行排序 排序时按小写字母排序
    l = sorted(os.listdir(path), key=str.lower)
    # get basename
    bn = os.path.basename(path)  # basename
    
    # 目录树中的前缀变量初始化
    pre = '|   '
    pre_f = '|-- '
    pre_f2 = '\-- '
    
    # 处理basename的打印方式
    # if `path=/user/foo` then `basename=foo`
    if depth == 0:
        print(bn)
    else:
        if len(l) == 0:
            pre_f = pre_f2
        s = pre * (depth - 1) + pre_f + bn
        print(s.lstrip())

    # 处理目录list中的iterm
    for f in l:
        if os.path.isfile(os.path.join(path, f)):
            # handle file
            if l.index(f) + 1 == len(l):
                pre_f = pre_f2
            s = pre * depth + pre_f + f + ' [file]'
            print(s.lstrip())
        else:
            # handle directory
            # recursion
            dirtree(os.path.join(path, f), depth + 1)

if __name__ == '__main__':
    import sys
    dirtree(sys.argv[1])

