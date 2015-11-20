# -*- coding: utf8 -*-


class Timing:

    """decorator class 计算函数执行时间 打印到控制台 单位毫秒
    """

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
