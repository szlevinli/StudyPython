class A:
  name = 'I am class A'
  attr1 = 'class A attribute is attr1'

  def __init__(self, parName='anymore', parAge = 10):
    self.name = parName
    self.age = parAge

print('A.name =', A.name)

a1 = A()
a2 = A('lhq', 100)
a3 = A('wwj', 16)

# 对象属性覆盖类属性
print('a1.name = {}, a1.age = {}'.format(a1.name, a1.age))
print('a2.name = {}'.format(a2.name))
print('a3.name = {}'.format(a3.name))

# 对象属性沿用类属性
print('a1.attr1 = {}'.format(a1.attr1))
print('a2.attr1 = {}'.format(a2.attr1))
print('a3.attr1 = {}'.format(a3.attr1))

# 增加新的对象属性
a1.other = 'other'
print('a1.other = {}'.format(a1.other))


