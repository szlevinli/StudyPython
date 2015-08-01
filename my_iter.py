########################
# 理解iterator
#
# 如果需要编写一个具有iteratble的iterator类，则必须实现以下两个函数
# __iter__
# __next__
########################


class yrange:

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class zrange_iter:

    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class zrange:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)


class reverse_iter:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

if __name__ == '__main__':
    y = yrange(5)
    print('first list(y)')
    print(list(y))
    print('second list(y)')
    print(list(y))
    print('第二次list(y)时，返回空的list，这是因为y.__next__()已经没有item了！')

    print('*' * 10)

    print('但z不同，无论list(z)几次他都能返回item，因为y和z的__iter__()函数写法不同')
    z = zrange(5)
    print(list(z))
    print(list(z))
