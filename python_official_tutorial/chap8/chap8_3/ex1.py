while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except (RuntimeError, TypeError, NameError):
        pass

"""
1: First, the try clause (the statement(s) between the try
and except keywords) is executed.
2: If no exception occurs, the except clause is skipped and execution of
the try statement is finished.
3: If an exception occurs during excution of the try clause, the rest of
the clause is skipped. Then if its type matches the exception named after the except
keyword, the except clause is executed, and then execution continues after the try statement.
4: If an exception occurs which does not match the exception named in the except clause, it is
passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops
with a message as shown above.
"""



"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/pytho(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_(base) zcw@mukoe(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python ex1.py
Please enter a number: 12
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python ex1.py
Please enter a number: str
Oops!  That was no valid number.  Try again...
Please enter a number: kddkj
Oops!  That was no valid number.  Try again...
Please enter a number: None
Oops!  That was no valid number.  Try again...
Please enter a number: zero
Oops!  That was no valid number.  Try again...
Please enter a number: 0
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python ex1.py
Please enter a number: ^CTraceback (most recent call last):
  File "ex1.py", line 3, in <module>
    x = int(input("Please enter a number: "))
KeyboardInterrupt
"""