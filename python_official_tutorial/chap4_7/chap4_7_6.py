"""
Some annonymous functions can
be create with the lambda keyword. This
function returns the sum of its two arguments:
lambda a,b: a+b. Lambda functions can be used
whereever function objects are required. They
are syntactically restricted to a single expression.
Semantically, they are just syntactic sugar for
a normal function definition. Like nested function
definitions, lambda functions can reference variables from the
containing scope:
"""

#Use it to return a function: 
def make_incrementor(n):
    return lambda x:x+n

f = make_incrementor(42)
print(f(0))

f1= make_incrementor("jack")
print(f1("son of bitch"))

#Use it to pass a small function as an argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')] #a tuple of pairs
pairs.sort(key = lambda pair:pair[1])
print(pairs)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python chap4_7_6.py
42
son of bitchjack
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
"""