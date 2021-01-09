(base) zcw@mukoedo1993:~$ #Python knows a number of compound data types,
(base) zcw@mukoedo1993:~$ #used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
(base) zcw@mukoedo1993:~$ squares =[1, 4, 9, 16, 25]

Command 'squares' not found, did you mean:

  command 'ksquares' from snap ksquares (20.04.0)
  command 'ksquares' from deb ksquares (4:19.12.3-0ubuntu1)

See 'snap info <snapname>' for additional versions.

(base) zcw@mukoedo1993:~$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> squares = [1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> #Like strings (and all other built-in sequence types) , lists can be indexed and sliced:
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares[0]  #indexing returns the item
1
>>> squares[-3: ] #slicing returns a new list
[9, 16, 25]
>>> # All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list: 
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36,49,64,81,100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> # Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
>>> cubes= [1, 8, 27, 65, 125] #somthing's wrong here
>>> 4**3
64
>>> #the cube of 4 is 64, not 65!
>>> cubes[3]=64
>>> cubes
[1, 8, 27, 64, 125]
>>> ####################
>>> You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
  File "<stdin>", line 1
    You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
        ^
SyntaxError: invalid syntax
>>> # You can also new items at the end of the list, by using the append() method (we will see more about methods later):
>>> cubes.append(216)
>>> cubes.append(7**3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> letters = ['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5]=['C','D','E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5]=[]
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:]=[]
>>> letters
[]
>>> letters = ['a','b','c','d']
>>> len(letters)
4
>>> a=['a','b','c']
>>> n=[1, 2, 3]
>>> x=[a,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> # Fibonacci series:
>>> # the sum of two elements defines the next
>>> a,b =0,1
>>> while a<10:
...     print(a)
...     a,b =b,a+b
... 
0
1
1
2
3
5
8
>>> i =256*256
>>> print('THe value of i is:', i)
THe value of i is: 65536
>>> a,b=0,1
>>> while a<1000:
...     print(a,end=',')
...     a,b=b,a+b
... 
>>> a1,b1=0,1
>>> while a1<1000:
...     print(a1,end=',')
...     a1,b1=b1,a1+b1
... 
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,>>> 

