# Function annotations: the type of return value and parameters


def f(ham: str, eggs: str ='eggs') -> str:
    print("Annotations",f.__annotations__)
    print("Arguments",eggs,ham)
    return ham+"and"+eggs

f('spam')

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python chap4_7_8.py
Annotations {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments eggs spam
"""