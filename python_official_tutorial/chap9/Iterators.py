for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)

for line in open("myfile.txt"):
    print(line, end='')


print("\nsecond part:\n")
s='abc'

it = iter(s)

print(it)

for i in range(4):
    print(next(it))



"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python Iterators.py
1
2
3
1
2
3
one
two
1
2
3
hehe 
caonima
fukku
tsunami
huridukeshi
second part:

<str_iterator object at 0x7f9db363d4f0>
a
b
c
Traceback (most recent call last):
  File "Iterators.py", line 25, in <module>
    print(next(it))
StopIteration
"""