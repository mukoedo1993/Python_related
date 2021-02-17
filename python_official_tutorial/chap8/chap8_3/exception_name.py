#

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))       # the exception instance
    print(inst.args)        # arguments stored in .args
    print(inst)             # __str__ allows args to be printed directly,
                            # but may be overridden in exception subclasses
    x, y = inst.args        #unpack args
    print('x = ',x)
    print('y =', y)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python exception_name.py
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x =  spam
y = eggs
"""