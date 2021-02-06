def foo(name,**kwds):
    return 'name' in kwds

#There is no possible call that will make it return True
#as the keyword 'name' will always bind to the first parameter.

#foo(1, **{'name':2})
"""
Traceback (most recent call last):
  File "chap4_7_3.py", line 7, in <module>
    foo(1, **{'name':2})
TypeError: foo() got multiple values for argument 'name'
"""

#But using But using / (positional only arguments),
#  it is possible since it allows name as a positional argument and 'name' as a key in the keyword arguments:

def foo1(name,/,**kwds):
    return 'name' in kwds

print(foo1(1, **{'name':2}))#True


def concat(*args, sep='/'):
    return sep.join(args)

tmp1=concat("earth","Mars","Venus")
print(tmp1)#earth/Mars/Venus

tmp2=concat("earth","Mars","Venus",sep=' ')
print(tmp2)#earth Mars Venus