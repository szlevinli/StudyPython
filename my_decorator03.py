def entryExit(f):
    print('enter entryExit function')
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f


@entryExit
def func1():
    print("inside func1()")


@entryExit
def func2():
    print("inside func2()")

print('start...')
func1()
func2()
print("func1.__name__ is", func1.__name__)
