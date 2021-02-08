###########################More on modules###############################
"""
A module can contain executable statements as well as function
definitions. These statements are intended to initialize the module.
They are executed only the first time the module name is encountered
in an import statement. 
"""

#A variant of import statement that imports names from a module directly
#into the importing module's symbol table.

from fibo import fib, fib2
print(fib(500))

#You could even
#from fibo import *
#This imports all names except those beginning with an underscore(_).
#In most cases Python programmers do not use this facility since it introduces
#an unknown set of names into the interpreter, possibly hiding some things
#you have already defined.
"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap6_Modules$ python sec6_1.py
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
None
"""