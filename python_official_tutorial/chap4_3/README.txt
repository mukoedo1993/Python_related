(base) zcw@mukoedo1993:~/Desktop$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = int(input("Please enter an integer"))
Please enter an integer 42
>>> 
>>> 
>>> import copy
>>> users={ 'Sato':'active',
...         'James': 'inactive',
...         'Jackson': 'active'}
>>> copy1 = users.copy()
>>> copy2 = copy.deepcopy(users)
>>> for user,status in users.copy().items():
...     if status == 'inactive':
...     del users[user]
  File "<stdin>", line 3
    del users[user]
    ^
IndentationError: expected an indented block
>>> for user , status in users.copy().items():
...     if status == 'inactive':
...             del users[user]
... 
>>> for user , status in copy1.copy().items():
...     print(user, status)
... 
Sato active
James inactive
Jackson active
>>> for u, s in copy2.copy().items():
...     print(u,s)
... 
Sato active
James inactive
Jackson active
>>> for user, status in users.copy().items():
...     print(user,status)
... 
Sato active
Jackson active
>>> ###Let's check the id:
>>> id(users)
140590919344192
>>> if(copy1)
  File "<stdin>", line 1
    if(copy1)
            ^
SyntaxError: invalid syntax
>>> id(copy1)
140590919344256
>>> id(copy2)
140590918197312
>>> #users, copy1 and copy2 all have different ids.
>>> #users, copy1 and copy2 all have different ids.
>>> lst1=[1, 5, 6, 7, 10]
>>> lst2=list(lst1)
>>> id(lst1)
140590918197760
>>> id(lst2)
140590918198656
>>> lst3= lst2
>>> id(lst3)
140590918198656
>>> #Only assignment directly is pass by reference, use the ...(...)

