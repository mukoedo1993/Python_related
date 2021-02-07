basket = {'apple', 'orange', 'apple', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)

print('grape' in basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print(a) # unique letters in a

tmp1 = a-b 
print(tmp1) #letters in a but not in b

tmp2 = a|b
print(tmp2)#letters in a or b or both

tmp3 =a &b
print(tmp3)#letters in both a and b

tmp4 = a^b
print(tmp4) #letters in either a or b but not in both


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

a1_tmp=set()
for x in 'abracadabra':
    if x not in 'abc':
        a1_tmp.add(x)
print(a1_tmp)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_4$ python set.py
{'apple', 'orange', 'banana', 'pear'}
True
False
{'c', 'b', 'a', 'd', 'r'}
{'r', 'b', 'd'}
{'c', 'b', 'z', 'l', 'm', 'a', 'd', 'r'}
{'c', 'a'}
{'l', 'm', 'b', 'r', 'z', 'd'}
{'d', 'r'}
{'d', 'r'}
"""