(base) zcw@mukoedo1993:~$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> #The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. e.g.: 
>>> while True: 
...     pass #Busy-wait  for keyboard interrupt(Ctrl+C)
... 
KeyboardInterrupt
>>> 
>>> ####
>>> #This is commonly used for creating minimal classes:
>>> class MyEmptyClass:
...     pass
... ###Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level. The pass is silently ignored:
... 
>>> def initlog(*args):
...     pass #Remember to implement this!
... 
>>> 

