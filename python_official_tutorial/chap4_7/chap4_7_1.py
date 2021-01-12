def ask_ok(prompt, retries=4, reminder= 'Please try again!'):
	while True:
		ok = input(prompt)
		if ok in('y','ye','yes'):
		 return True
		if ok in('n','no','nop','nope'):
		 return False
		retries = retries - 1
		if retries <0:
		 raise ValueError('invalid user response')
		print(reminder)

"""
The function can be called in several ways:
1: Similar to C++
"""
i = 5
def f(arg=i):
	print(arg)

i = 6
f()
'''
Important warning: The default value is evaluated only once. This makes a 
difference when the default is a mutable object such as a list, dictionary, or 
instances of most classes. For example, the following function accumulates the
argument passed to it on subsequent calls:
'''
def f1(a,L=[]):
 L.append(a)
 return L
 
print(f1(1))
print(f1(2))
print(f1(3))

# If you don't want the default to be shared between subsequent calls, you can
# write the function like this instead: 
def f2(a,L=None):
 L = []
 L.append(a)
 return L
print(f2(1))
print(f2(2))
print(f2(3))
"""
log:
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python chap4_7_1.py
5
[1]
[1, 2]
[1, 2, 3]
[1]
[2]
[3]

"""
