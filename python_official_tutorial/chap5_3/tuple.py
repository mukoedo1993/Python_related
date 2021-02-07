t = 12345, 54321, 'hello!'
print(t[0])


print(t)


# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print(u)


# Tuples are immutable: 
#t[0] = 88888
"""
Traceback (most recent call last):
  File "tuple.py", line 14, in <module>
    t[0] = 88888
TypeError: 'tuple' object does not support item assignment
"""

# but they can contain mutable objects
v=([1, 2, 3], [3, 2, 1])
print(v)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_3$ python tuple.py
12345
(12345, 54321, 'hello!')
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
([1, 2, 3], [3, 2, 1])
"""
