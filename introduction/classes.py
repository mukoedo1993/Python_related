class Point:
    def __init__(self,x,y):#constructor
        self.x=x
        self.y=y # self is a reference to teh current object.

    def move(self):
        print("move")

    def draw(self):
        print("draw")



point114=Point(10,20)
point114.z=13
print(point114.x+point114.y)
print(point114.z)

class Person:
    def __init__(self,name):
        self.name=name # self references to the current object

    def talk(self):
        print("Hi! ")


nimasilese=Person("nimasile")
print(nimasilese.name)