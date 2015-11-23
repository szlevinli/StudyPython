# -*- coding: utf8 -*-


from decorator.decorator import Timing
import re


@Timing
def copy(fromFile, toFile):
    with open(fromFile, mode='r', encoding='utf8') as r, \
            open(toFile, mode='w') as w:
        for line in r:
            w.writelines(line)


@Timing
def copy2(fromFile, toFile):
    read_size = 1024 * 1024 * 4
    with open(fromFile, mode='r', encoding='utf8') as r, \
            open(toFile, mode='w') as w:
        while True:
            lines = r.readlines(read_size)
            if not lines:
                break
            resql(lines, 10)
            w.writelines(lines)


@Timing
def resql(lines, max_lines):
    i = 0
    j = 0
    p = re.compile('(INSERT INTO .*\) VALUES )', re.I)
    p2 = re.compile(';$')
    for line in lines:
        m = p.search(line)
        if m is not None:
            k = j % max_lines
            if k == 0:
                line = p2.sub(',', line)
            elif k == max_lines - 1:
                line = p.sub('', line)
            else:
                line = p.sub('', line)
                line = p2.sub('', line)
            j += 1
        lines[i] = line
        i += 1


if __name__ == '__main__':
    import sys
    copy2(sys.argv[1], sys.argv[2])
