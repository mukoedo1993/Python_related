"""
The str() function is meant to return representations
of values which are fairly human-readable, while repr()
is meant to generate represenattions which can be read by
the interpreter (or will force a SyntaxError if there is
no equivalent syntax). For objects which don't have a particular
representation for human consumption, str() will return the same value
as repr(). Many values, such as numbers or structures like lists 
and dictionaries, have the same representaion using either function.
Strings, in particular, have two distinct representations.
"""

s = 'Hello world'
print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y)+'...'
print(s)

#The repr() of a string adds string quotes and backslashes:
hello = 'hello,world\n'
hellos = repr(hello)
print(hellos)

#The argument to repr() may be any Python object:
print(repr((x,y,('spam','eggs'))))

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_1$ python str_and_repr.py
Hello world
'Hello world'
0.14285714285714285
The value of x is 32.5, and y is 40000...
'hello,world\n'
(32.5, 40000, ('spam', 'eggs'))
"""