"""
Private instance variables that cannot be 
accessed except from inside an object don't
exist in Python. However, there is a convention
that is followed by most Python code: a name prefixed
with an underscore (e.g. __spam) should be treated as 
a non-public part of the API(whether it is a function, a method
or a data member.) It should be considered an implementation
detail and subject to change without notice.


Since there is a valid use-case for class-private memebers(namely to avoid 
name clashes of names with names defined by subclasses), there is limited support 
for such a mechanism, called name mangling. Any identifier of the form __spam(at least two
leading underscores, at most one trailing underscore) is textually replaced with _classname__spam,
where classname is the current class name with leading underscore(s) stripped. This mangling is done
without regard to the syntactic position of the identifier, 
"""

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)#here, __update is a private member for Mapping. In order to it, you need: _Mapping__update

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    
    def update(self, keys,values):
        #provide new signature for update
        #but does not break __init_-()
        for item in zip(keys,values):
            self.items_list.append(item)

ob1 = MappingSubclass([12,23,28,2737])
ob1.update({13,24,36},[32,37,-237])
for it in ob1.items_list:
    print(it)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python private_variables.py
12
23
28
2737
(24, 32)
(36, 37)
(13, -237)
"""