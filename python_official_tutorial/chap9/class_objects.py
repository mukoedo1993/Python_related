class MyClass:
    """A simple example class"""
    i = 12345


    def f(self)->str:
        return 'hello world'

hehe = MyClass()
print(hehe.__doc__)
print(hehe.f())

xf = hehe.f
i = 0
while True:
    i+=1
    if(i>10):
        break
    print(xf())
#In the MyClass example, this will return the string 'hello world'

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python class_objects.py
A simple example class
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
"""