class A:

  def __init__(self):
    self.normalAttr = 'normal attribute'
    self.__privateAttr = 'private attribute'

  def getPrivateAttr(self):
    return self.__privateAttr

a = A()

try:
  print('a.__privateAttr  = {}'.format(a.__privateAttr))
except:
  print('a.__privateAttr is not exists.')

print('a._A__privateAttr = {}'.format(a._A__privateAttr))

print('a.getPrivateAttr() = {}'.format(a.getPrivateAttr()))

a.__privateAttr = 'new value'

print('a._A__privateAttr = {}'.format(a.__privateAttr))
