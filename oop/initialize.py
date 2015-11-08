class Cat:
    name = 'cat'

    def __init__(self, name):
        self.name = name

missy = Cat('Missy')
lucky = Cat('Lucky')

print(missy.name)
print(lucky.name)

print(Cat.name)
print(missy.__class__.name)
print(lucky.__class__.name)
