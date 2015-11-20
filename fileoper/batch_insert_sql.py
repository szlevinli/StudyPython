# -*- coding: utf8 -*-


class Timing:

    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        from datetime import datetime
        start_dt = datetime.now()
        self.f(*args, **kwargs)
        end_dt = datetime.now()
        speed_millis = (end_dt - start_dt).total_seconds() * 1000
        print("call [%s] function elapsed time is [%f] milliseconds " %
              (self.f.__name__, speed_millis))


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
            w.writelines(lines)

if __name__ == '__main__':
    import sys
    copy2(sys.argv[1], sys.argv[2])

