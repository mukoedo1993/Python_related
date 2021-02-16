import math
print(f'The value of pi is approximately {math.pi:.3f}')
#Passing an integer after the ':' will cause that field
#to be a minimum number of characters wide. This is useful for
# making columns line up.


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

#Other modifiers can be used to convert the value before it is formatted.
#'!a' applies ascii(), '!s' applies str(), and '!r' applies repr()

animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of{animals!r}')
"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_1$ python formatted_string_literals.py
The value of pi is approximately 3.142
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
My hovercraft is full of eels.
My hovercraft is full of'eels'
"""