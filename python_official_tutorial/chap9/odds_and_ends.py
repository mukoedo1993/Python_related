# Odds and Ends
# A piece of Python code that expects a particular abstract
# data type can often be passed a class that emulates the
#methods of that data type instead. For instance, if you have
#a function that formats some data from a file object, you can
#define a class with methods read() and readline() that get the
# data from a string buffer instead, and pass it as an argument.


"""
Instance method objects have attributes, too: m.__self__ is the instance
object with the method m(), and m.__func__ is the function object corresponding
to the method.
"""


class Employee:
    pass

john = Employee()  #Create an empty employee record

# Fill the fileds of the record
john.name = 'John Doe'
john.debt = 'compute lab'
john.salary = 1000
