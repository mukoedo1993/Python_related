#Exception class can be defined which do anything
#other class can do, but are usu. kept simple, often 
# only offering a number of attributes that allow information
#  about the error to be extracted by handlers for the exception.
#When creating a module that can raise several distinct errors, a common
# practice is to create a base class for exceptions defined by that module, 
# and subclass that to create specific exception classes for different error
# conditions:

class Error(Exception):
    """Base class for exceptions in this module"""
    pass

class InputError(Error):
    """Exception raised for errors in the input

    Attributes:
        expression -- input expression in which the error
        message -- explanation of the error
    """

    def __init__(self,expression,message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's
    not allowed.

    Attributes:
        previous --  state at begining of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


ob1=TransitionError(12,23,'skdhj')
print(id(ob1))
print(ob1.previous)
print(id(ob1.next))

raise InputError(13,4938)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8$ python chap8_6_user_defined_exceptions.py
139679594206496
12
94164196200448
Traceback (most recent call last):
  File "chap8_6_user_defined_exceptions.py", line 48, in <module>
    raise InputError(13,4938)
__main__.InputError: (13, 4938)
"""