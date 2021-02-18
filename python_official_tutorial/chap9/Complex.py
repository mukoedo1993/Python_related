class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# instance Objects
"""
There are two kinds of valid attribute names:
data structures and methods.

data attributes correspond to "instance variables"
 in Smalltalk, and to "data members" in C++.
 Data attributes need be declared; like local variables,
 they spring into existence when they are first assigned to.
 For example, if x is the instance of MyClass created above, 
 the following piece of code will print the value 16, without
 leaving a trace:
"""

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


#(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python Complex.py
#3.0 -4.5
#16