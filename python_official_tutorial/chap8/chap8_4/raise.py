try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    #If you need to determine whether an exception
    #was raised but don't intend to handle it,
    #a simpler form of the raise statement allows
    # you to re-raise the exception:
    raise

#The sole argument to raise indicates the exception to be raised.
# This must be either an exception instance or an exception class
#(e.g. a class that derived from Exception). If an exception class is passed,
# it will be implicitly instantiated by calling its constructor with
# no arguments:

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_4$ python raise.py
An exception flew by!
Traceback (most recent call last):
  File "raise.py", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere
"""