
class Dog:

    tricks = []             # mistaken use of a class variable
    name=""

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("dog1")
e = Dog("dog2")

d.add_trick("walk")
e.add_trick("bark")

print(d.tricks,d.name)
print(e.tricks,e.name)
# The below line through an error
print(Dog.tricks,Dog.name)