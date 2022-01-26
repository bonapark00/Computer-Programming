Lab 13 final answers by Park Jaeyeon, student ID 2020147519

Answer Q1:
(a) The purpose of escape sequences is to display a character
which cannot be displayed directly. For example, if we want to
print '(single quote) inside the string, it should be distinguished
from quotes used to separate strings. So, we need to escape sequence
starting with backslash(\) i.e. \' would print single quote.

(b)
'\N{HANGUL SYLLABLE TAEG}'.encode() equates to b'\xed\x83\x9d'.
ed 83 9d is number in hexadecimal, and it represents file size to be 3 byte.

(c) UTF-8 encoding uses 1 to 4 bytes to represent a single Unicode character.
If the code point is < 128, it’s represented by the corresponding byte value.
If the code point is >= 128, it’s turned into a sequence of two, three, or four bytes,
where each byte of the sequence is between 128 and 255.
The reason UTF-8 is designed to have this property is
to ensure that the byte representation for one character is not part of the byte representation for another character in any case.

Answer Q2:
(a) 'IndexError: list index out of range', index error, occurs in given code.
For loop in 3 line iterates from loop variable i 0 to loop variable i  4(len(x) = 5).
In 1st iteration(i = 0), x[0] value equals 1, then it doesn't satisfy if condition in line 4.
In 2nd iteration(i = 1), x[1] value equals 2, satisfying if condition, then deleting element 2 in list x.
Then list x becomes [1,3,4,5]
In 3rd iteration(i = 2), x[2] value equals 4, satisfying if condition, then deleting element 4 in list x.
Then list x becomes [1,3,5]
In 4th iteration(i = 3), index 3 is out of range of list x indexes. The maximum index value in list x  is 2.
So python throw IndexError.

(b)
If I assume that the purpose of given program is to delete all even numbers in list x,
I can modify the code like the code below.
# List code snippet
x = [1, 2, 3, 4, 5]
j = 0

for i in range(len(x)):
    if x[j] % 2 == 0:
        del x[j]
    else:
        j = j + 1
# code finish
This code above makes no IndexError,
because variable 'j' never becomes larger than the largest index number in list x.

Or, if I assume the program just wants to handle IndexError, I can use try block and exception handler.

Answer Q3.
Method is the object-oriented word for function.
Functions can be called in function(argument) format, i.e. add(1, 2)
'function' is the name of the called function, and 'argument' is providing values for parameters

There are 2 ways for calling a method. (1) object.method(argument), (2) class.method(object, argument)
'object' is where method is called, 'method' is the name of method to call,
'class' is name of class, 'argument' is the argument for method.

The self parameter is a reference to the current instance of the class.
It is used to access the attributes and methods of the class.
It binds the attributes with the given argument.


Answer Q4.
(a) none
(b) ValueError in line 3 is raised. Then in line 14, it is handled by ValueError exception handler.
(c) OverflowError in line 7 is raised. Then in line 16, it enters exception handler.
    But in line 17, OverflowError is re-raised by msg.
    Then it is handled in line 25.
(d) ValueError in line 12 is raised because int() cannot convert string with alphabets to int.
    Then in line 14, it is handled by ValueError exception handler.

Answer Q5. (S3)

Answer Q6.
Encapsulation: Encapsulation wraps data and methods. This puts restrictions on accessing
variables and methods directly. And it can prevent the modification of data.
So an object's variables can only be changed by an object's method.
Then those type of variables are called private variables.
You can convert a data or method attribute into private attribute by
prefixing a data or method attribute by double underbars(__), i.e self.__n
You can implement encapsulation by properties.
# Encapsulation code snippet
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
hi = A(1)
hi.a = 9
# code finish
@property is used to get the value of a private attribute without using any getter methods.
The name of the method is the name of the public attribute(a). It functions as the getter for attribute a.
@method_name.setter marks the method that sets value, in this case @a.setter
It is used to set the value of private variable.
From outside, you still use 'a' with object for setting the attribute.

Inheritance: A class can inherit methods and instance variables from another class.
Parent class(or superclass) inherits all methods and instance variables to child class(or subclass).
Inheritance is powerful feature in object oriented programming,
because it allows to define a new class with little or no modification to an existing class.

# Inheritance code snippet
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
# code finish
Novel is a subclass of Book class. Novel __init__ method calls the __init__ method of the Book class.
It is to initialize variable name from Book class, which is so convenient that there is no need for assigning existing variables in superclass again.
And it also initializes its own instance author in __init__ method.
Subclass can also add new method like getAuthor().

Polymorphism: Polymorphism means same function name with different signatures being used for different types.
It makes programmers easier to reuse the code and classes once written, tested and implemented.

# Polymorphism code snippet: function
print(len('Yonsei'))        # 6
print(len([1, 2, 3]))       # 3
# code finish
In this code above, inbuilt polymorphic function len() is used for both string and list.

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
In this code above, there is two classes Novel and Poetry.
They share the same method names 'name(name)',
so I can call the method without concerning about which class type each object is.

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
Polymorphism allows us to access overridden methods.
Overriding is re-defining a method from the superclass in subclass.
In code above, B is child class of A.
There is hello() method in both classes, and when we call hello() for object b,
hello() method for object b is overridden and method class B version of hello() method is called.

Answer Q7.
(a)
Using global variables in a function makes encapsulation in python meaningless,
breaks the natural scope of variable, and makes harmful side effects.
So to enforce encapsulation, it is reasonable to use classes, functions, parameters and the return keyword.

# Global keyword code snippet 1
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
print(a, b) # 2 2
# code finish

In code above, function foo1() uses global keyword and foo2() doesn't.
But in turn, both functions alters global variable values for a and b.
So instead of using global keyword, I can return the values of local variable a and b in foo2()
and assign those to global variable a and b.

Using classes, methods and attributes can also help.
The attributes on a class can be used by different methods on that class.
# Global keyword code snippet 2
def setUp():
    global name, age
    name = input('Name: ')
    age = input('Age: ')

class Person:
    def __init__(self):
        self.name = input('Name: ')
        self.age = input('Age: ')
# code finish
Instead of using functions, in order to eliminate side effects,
object oriented programming by using class is much better.


(b)
If I cannot use global keyword inside a function,
I can never mutate or access local variable in frame of global or other functions.
# Application of problem without global keyword.
def getArea(r):
    pi = 3.14
    area = pi*r**2

def getCircum(r):
    pi = 3.14
    circum = pi*r*2
# code finish
In code above, when using function, I cannot change 'pi' value outside of function.
For example, there can be cases when I want to use 'pi' value as 3.141592 for exact calculation.
But for doing that, I need to change all functions' local variable pi one by one.
It is very laboring work.
Also, if I want to use 'pi' variable outside functions, I  need to define new 'pi' variable in global frame.

Answer Q8.
Each time I call a function, Python make a new frame
which contains the function parameters and local variables.
Recursive function is a function that calls itself,
so each new function frame is created for each call.
When one function calls another function, the caller function is set on hold
and the called function becomes active.
# Recursion code snippet
def fact(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    else:
        return n * fact(n-1)
x = fact(3)
# code finish
Implementing fact(3) requires three calls to function fact().
If I call fact(3), it will in turn call fact(2), which will call fact(1).
So fact(1) returns 1 to the frame of fact(2).
Then fact(2) returns 2*1 to the frame of fact(3).
Lastly, fact(3) returns 3*2*1 which equates to 6.












