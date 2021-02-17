#finally:
"""
If a finally clause is present, the finally clause
will execute as the last task before the try
statement completes. The finally clause runs whether or not the try
statement produces an exception. The following points discuss more complex cases
when an exception occurs:

"""

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())


def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,1)

divide(2,0)

divide("2","1")


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8$ python chap8_7.py
False
result is 2.0
executing finally clause
division by zero!
executing finally clause
executing finally clause
Traceback (most recent call last):
  File "chap8_7.py", line 34, in <module>
    divide("2","1")
  File "chap8_7.py", line 22, in divide
    result = x/y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
"""