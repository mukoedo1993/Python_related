(base) zcw@mukoedo1993:~$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {"John": "inactive",
...             "Helen": "active",
...             "James": "active", #and so on...
...             }
>>> #Strategy:  Iterate over a copy:
>>> for user, status in users.copy().items():
...     if status == 'inactive':
...             del users[user]
... 
>>> #Startegy: Create a new collection
>>> active users = {}
  File "<stdin>", line 1
    active users = {}
           ^
SyntaxError: invalid syntax
>>> active_users = {}
>>> for user, status in users.items():
...     if status == 'active':
...             active_users[user] = status
... 
>>> for us, stts in active_users.items():
...     if stts == 'active':
...             print(us,stts)
... 
Helen active
James active
>>> 

