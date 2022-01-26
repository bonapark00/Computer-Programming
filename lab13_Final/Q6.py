class A:
    def __init__(self, a):
        self.a = a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a
        return self.a
##

class Book:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

class Novel(Book):
    def __init__(self, name, author):
        Book.__init__(self, name)
        self.author = author
    def getAuthor(self):
        return self.author

##

# Polymorphism code snippet: function
print(len('Yonsei'))        # 6
property(len([1, 2, 3]))    # 3
# code finish

# Polymorphism code snippet: Class methods
class Novel:
    def name(self, name):
        self.name = name
class Poetry:
    def name(self, name):
        self.name = name

a = Novel()
b = Poetry()
a.name('n')
b.name('p')
print(a.name, b.name)
# code finish

# Polymorphism code snippet: Method overriding
class A:
    def hello(self):
        print('hello() method from class A')
class B(A):
    def hello(self):
        print('hello() method form class B')
a = A()
b = B()

a.hello()   # output:  hello() method from class A
b.hello()   # output:  hello() method from class B
# code finish



