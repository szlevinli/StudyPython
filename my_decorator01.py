class MyDecorator():

    def __init__(self, f):
        print("inside MyDecorator.__init__()")
        f()

    def __call__(self):
        print("inside MyDecorator.__call__()")


@MyDecorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")
aFunction()
