class grandfather1():

    def f(self):
        print('grandfather1')


class grandfather2():

    def f(self):
        print('grandfather2')


class father1(grandfather1):

    def f2(self):
        print('father1')


class father2(grandfather2):

    def f(self):
        print('father2')


class me(father1, father2):

    def f2(self, a):
        print('me is', a)

if __name__ == '__main__':
    x = me()
    x.f()
    x.f2('good')
