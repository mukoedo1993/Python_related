"""
A class in an except clause is compatible with an exception
if it is the same class or a base class thereof (but not the other way around --
an except clause listing a derived class is not compatible with a base class).
"""

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

class B1(Exception):
    pass

class C1(B1):
    pass

class D1(C1):
    pass

for cls in [B1,C1,D1]:
    try:
        raise cls()
    except B1:
        print("B1")
    except C1:
        print("C1")
    except D1:
        print("D1")
"""
A class in an except clause is compatible with an exception
if it is the same class or a base class thereof (but not the other way around --
an except clause listing a derived class is not compatible with a base class). For example,
the following code will print B, C, D in that order:
"""  

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python ex2.py
B
C
D
B1
B1
B1
"""