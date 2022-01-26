a = 0
b = 0
def foo1():
    global a
    global b

    a = 1
    b = 1
foo1()
print(a, b) # 1 1



def foo2():
    a = 2
    b = 2
    return a, b
a, b = foo2()
print(a, b)
#######

# Class Using instead of global keyword
def setUp():
    global name, age
    name = input('Name: ')
    age = input('Age: ')

class Person:
    def __init__(self):
        self.name = input('Name: ')
        self.age = input('Age: ')
# code finish


# Application of problem without global keyword.
def getArea(r):
    pi = 3.14
    area = pi*r**2
# code finish






