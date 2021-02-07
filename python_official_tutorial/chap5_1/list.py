fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple','banana']
print(fruits.count('apple'))


print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana',4)) #Find next banan starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

print(id(fruits))

fruits.sort()
print(fruits)

tmp1 = fruits.pop()
print(fruits)
print(tmp1)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_1$ python list.py
2
0
3
6
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
140273705226432
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']
pear
"""
