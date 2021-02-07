tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)


del tel['sape']
tel['irv'] = 4127
print(tel)


tel1 = list(tel)
print(tel1)

sorted(tel)
print(tel)

print('guido' in tel)

print('jack' not in tel)


print(dict([('sape', 4139),('guido', 4127),('jack', 4098)]))
#a list of two-element tuples
#convert the list into a dict.
# Then, print out the list.

#In addition,
print({x:x**2 for x in(2,4,6)})

x1={}
for x in(2,4,6):
    x1[x]=x**2
print(x1)


x1__ = {x:x1[x] for x in x1 if x != 2}
print(x1__)

del x1[2]
print(x1)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_5$ python dict.py
{'jack': 4098, 'sape': 4139, 'guido': 4127}
{'jack': 4098, 'guido': 4127, 'irv': 4127}
['jack', 'guido', 'irv']
{'jack': 4098, 'guido': 4127, 'irv': 4127}
True
False
{'sape': 4139, 'guido': 4127, 'jack': 4098}
{2: 4, 4: 16, 6: 36}
{2: 4, 4: 16, 6: 36}
{4: 16, 6: 36}
{4: 16, 6: 36}
"""