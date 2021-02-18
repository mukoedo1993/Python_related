#Generally speaking, instance variables are for
#data unique to each instance and to class variables are
#for attributes and methods shared by all instances of the class:

class Dog:
    kind = 'canine'         #class variable shared by all instances

    def __init__(self, name):
        self.name = name        # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                          # shared by all dogs
print(e.kind)                          # shared by all dogs

print(d.name)                          # unique to d
print(e.name)#unique to e


#################Another example##################
class Dog1:
    def __init__(self, name):
        self.name = name
        self.tricks = []        # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog1('Fido')
e = Dog1('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

###A mistaken use of Dog1, let's name it Dog1_1:

class Dog1_1:

    tricks = []

    def __init__(self, name):
        self.name = name
    
    def add_trick(self,trick):
        self.tricks.append(trick)
    
d1 = Dog1_1('Fido')
e1 = Dog1_1('Buddy')
d1.add_trick('roll over')
e1.add_trick('play dead')
print(d1.tricks)                 # unexpectedly shared by all dogs
"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python Dog.py
canine
canine
Fido
Buddy
['roll over']
['play dead']
['roll over', 'play dead']
"""