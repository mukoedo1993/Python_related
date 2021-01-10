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
>>> 
