def fib(n):
    a, b = 0, 1
    while a < n:
        print("a = {} b = {}".format(a, b))
        a, b = b, a + b
    print()


def fib2(n):
    a = 0
    b = 1
    while a < n:
        print("a = {} b = {}".format(a, b))
        a = b
        b = a + b
    print()


def fib3(n):
    a = 0
    b = 1
    while a < n:
        print("a = {} b = {}".format(a, b))
        c = a + b
        a = b
        b = c
    print()

if __name__ == "__main__":
    fib(100)

