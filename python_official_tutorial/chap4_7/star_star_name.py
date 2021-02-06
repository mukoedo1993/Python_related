"""
When a final formal parameter of the form **name is present,
it receives a dictionary (see Mapping Types -- dict) containing
all keyword arguments except for those corresponding to a 
formal parameter. This may be combined with a formal parameter of
the form *name (described in the next subsection) which receives a tuple
containing the positional arguments beyond the formal parameter list.
(*name must occur before **name.) For example, if we define a function
like this:
"""


def cheeseshop(kind, *arguments, **keywords):
    #        *arguments <-> positional arguments
    #        **keywords <-> keyword arguments (in the form of dictionary)
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger","It's very funny, Sir.",
           "It's REALLY VERY VERY FUNNY, sir",
           shopkeeper = 'Michael Palin',
           client = 'John Cleese',
           sketch = 'Cheese Shop Sketch'
           )


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python star_star_name.py
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very funny, Sir.
It's REALLY VERY VERY FUNNY, sir
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
"""