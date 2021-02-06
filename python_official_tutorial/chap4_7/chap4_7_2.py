#Functions can be called with keyword arguments of the form kwarg = value.


def parrot(voltage, state= 'a stiff', action = 'voom', type= 'Norweigan Blue'):
    print("this parrot wouldn't",action, end='')#The end value is'\n' by default
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)     #1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=100000, action = 'VOOOOOOOM') # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

"""
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
"""

"""
In a function call, keyword arguments must follow positional arguments.
 All the keyword arguments passed must match one of the arguments accepted by the function 
 (e.g. actor is not a valid argument for the parrot function), and their order is not important. 
 This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too).
 No argument may receive a value more than once. Here’s an example that fails due to this restriction:
"""
