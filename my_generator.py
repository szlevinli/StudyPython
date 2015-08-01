#######################################
# 理解generator
# 函数中有 yield 这个关键字 这个函数就会返回一个generator对象
#######################################


def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


def test_yrange():
    y = yrange(3)  # 调用yrange函数后立刻返回一个generator对象 此时函数内部代码还未执行
    print(y)  # <generator object yrange at 0x102a7a3f0>
    print(next(y))  # generator和iterator类似可以使用next()去获取下一个item
    print(next(y))
    print(next(y))
    print(next(y))

# generator内部运作演示
# call funciton时返回generator对象，但不执行函数体内代码
# 首次调用next()函数后开始执行函数体内代码到yield为止
# 再次调用next()函数后接着执行yield后的代码到下一个yield为止
# 再再次调用next()函数执行方式与上一条一致，直到StopIteration


def foo():
    print('begin')
    for i in range(3):
        print('befor yield', i)
        yield i
        print('after yield', i)
    print('end')


def test_foo():
    f = foo()
    next(f)
    next(f)
    next(f)
    next(f)
