(base) zcw@mukoedo1993:~$ python
Python 3.8.3 (default, Jul  2 2020, 16:21:59) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+2
4
>>> 50-5*6
20
>>> (50-5*6)/4
5.0
>>> 8/5 #division always returns a floating point number
1.6
>>> 17/3
5.666666666666667
>>> 17//3  # floor division discards the fractional part
5
>>> 17%3
2
>>> #The division above returns the remainder of division
>>> #
>>> #
>>> 5 ** 2 #5 squared
25
>>> 2 ** 7 #2 to the power of 7
128
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>> n # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> #############
>>> # In interactive mode, the last printed expression is assigned to the
>>> #variable _. This means that when you are using Python as a desk calculator,
>>> #it is somewhat easier to continue calculations, for example:
>>> tax =12.5/100
>>> price=100.50
>>> price*tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> #This variable should be treated as read-only by the user. Don't explicitly assign a value to it -- you would create an independent local variable with the same masking the built-in variable with its magic behavior.
>>> #This variable should be treated as read-only by the user. Don't explicitly assign a value to it -- you would create an independent local variable with the same masking the built-in variable with its magic behavior.
>>> #In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part. (e.g. 3+5j)
>>> #
>>> 3+5j+(6+8j)
(9+13j)
>>> 3+5J+6+8.7j
(9+13.7j)
>>> 
