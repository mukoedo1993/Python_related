import fibo
fibo.fib(1000)


print(fibo.fib2(100))


#A module is a file containing Python definitions and statements.
#The file name is the module name with the suffix.py appended. Within
# a module, the module's name (as a string) is available as the value of
#the global varibale __name__. 
print(fibo.__name__)


#If you intend to use a function often you can assign it to 
#a local name:

fib = fibo.fib
fib(500)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap6_Modules$ python import_module.py
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fibo
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
"""