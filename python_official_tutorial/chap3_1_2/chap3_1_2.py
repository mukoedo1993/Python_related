(base) zcw@mukoedo1993:~$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 'spam eggs' #single quotes
'spam eggs'
>>> 'doesn\t' # use \' to escape the single quote
'doesn\t'
>>> '"Yes," they said.'
'"Yes," they said.'
>>> '"Isn\'t" they said.'
'"Isn\'t" they said.'
>>> '"Isn\"t" they said.'
'"Isn"t" they said.'
>>> # the '\' character could be used to escape...
>>> '"Isn\'t" they said.'
'"Isn\'t" they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.' 
>>> s #without print() \n is included in the output
'First line.\nSecond line.'
>>> print(s)
First line.
Second line.
>>> #If you DON'T WANT characters prefaced by \ to be interpreted as special
>>> #characters, you can use raw strings by adding an r before the first quote:
>>> print('C:\some\name') # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name') #note the r before the quote
C:\some\name
>>> ###
>>> #String literals can span multiple lines. 
>>> #One way is using triple quotes: """...""" or  '''...'''. End of lines are
>>> #automatically included in the string, but it's possible to prevent this
>>> # by adding a \ at the end of the line. The following example:
>>> print("""\)
... Usage thingy [OPTIONS]
... -h                          Display this usage message
... -H                          Hostname to connect to
... """)
\)
Usage thingy [OPTIONS]
-h              		Display this usage message
-H                          Hostname to connect to

>>> # 3 times 'un', followed by 'ium'
>>> 3*'un'+'ium'
'unununium'
>>> # Two or more string literals (i.e. the one enclosed between the quotes) next to each other are automatically concatenated.
>>> # This feature is particularly useful when you want to break long strings:
>>> text = ('Put several strings within parentheses ')
>>> text =('Put several strings within parentheses '
...        ' to have them joined together.')
>>> text
'Put several strings within parentheses  to have them joined together.'
>>> # This only works with two literals though, not with variables or expressions
>>> prefix ='Py'
>>> prefix 'thon'
  File "<stdin>", line 1
    prefix 'thon'
           ^
SyntaxError: invalid syntax
>>> prefix + 'thon'
'Python'
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> #Indices may also be negative numbers, to start counting from the right: 
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> #Note that the indices support the negative index (-1 means the rightmost,)>>> #-2 means the one on the left side of index[-1], and so forth.
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[:2] #character from the beginning to position 2 (excluded)
'Py'
>>> word[4:] #characters from position 4 (included) to the end
'on'
>>> word[-2:] #characters from the second-last (included) to the end
'on'
>>> #left-inclusive####basically
>>> ############################3
>>> # Attempting to use an index that is too large will result in an error:
>>> word[42]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> ################
>>> #Howevr, out of range slice indexes are handled gracefully when used for slicing
>>> word[4:42]
'on'
>>> word[42:]
''
>>> ####################
>>> ###################3
>>> ###################
>>> #Python strings cannot be changed --they are immutable. Therefore, assigning to an indexed position in the string results in an error:
>>> word[0]='J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 'J' +word[1:]
'Jython'
>>> word[:2]+'py'
'Pypy'
>>> #The built-in function len() returns the length of a string: 
>>> s='supercalifragilisticeexpialidocious'
>>> len(s)
35
>>> ####If you want to use a new string, you should create a new one:
>>> 'J' +word[1:]
'Jython'
>>> word[:2] +'py'
'Pypy'
>>> 
