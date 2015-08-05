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
    l = sorted(os.listdir(path), key=str.lower)
    bn = os.path.basename(path)  # basename
    pre = '|   '
    pre_f = '|-- '
    pre_f2 = '\--'
    if depth == 0:
        print(bn)
    else:
        if len(l) == 0:
            pre_f = pre_f2
        s = pre * (depth - 1) + pre_f + bn
        print(s.lstrip())
    for f in l:
        if os.path.isfile(os.path.join(path, f)):
            if l.index(f) + 1 == len(l):
                pre_f = pre_f2
            s = pre * depth + pre_f + f + ' [file]'
            print(s.lstrip())
        else:
            dirtree(os.path.join(path, f), depth + 1)
