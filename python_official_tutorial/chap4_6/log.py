(base) zcw@mukoedo1993:~$ # sec4_6: Defining Functions:
(base) zcw@mukoedo1993:~$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def fib(n):
... #Write Fibonacci series up to n
...  """Print a Fibonacci series up to n."""
...     a, b = b, a+b
  File "<stdin>", line 4
    a, b = b, a+b
                ^
TabError: inconsistent use of tabs and spaces in indentation
>>> def fib(n): #write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a<n:
...             print(a, end=' ')
...             a, b = b, a+b
...     print()
... 
>>> fib(16)
0 1 1 2 3 5 8 13 
>>> fib(3)
0 1 1 2 
>>> #Now call the function once again we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
>>> ####################
>>> #The keyword def introduces a function definition. It must be followed by
>>> #the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.
>>> ############## The first statement of the function body can optionally be a string literal; this string literal is the function's documentation string, or d-ocstring.
>>> ##############
>>> """The execution of a function"""
'The execution of a function'
>>> ####The execution of a function introduces a new symbol table used for localvariables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement), although they may be referenced.
>>> fib
<function fib at 0x7fbaecd43310>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89 
>>> # Even functions without a return statement do return a value, albeit a rather boring one. This value is called None(it's a built-in name)
>>> fib(0)

>>> print(fib(0))

None
>>> def fib2(n):
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a<n:
...      result.append(a)       #see below
...      a, b = b, a+b
...     return result
... 
>>> f100 = fib2(100)
>>> f100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> 
