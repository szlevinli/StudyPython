# -*- coding: utf8 -*-


def copy(fromFile, toFile):
    lines = 56
    with open(fromFile, mode='r', encoding='utf-8') as r, \
            open(toFile, mode='w') as w:
        buffers = r.readlines(lines)
        print(type(buffers))
        print(buffers)
        #for line in r.readlines(100):
            # buffers.append(line)
        #    print(type(line))
        #    print(line)
        w.writelines(buffers)

if __name__ == '__main__':
    copy("f.csv", "t.csv")
