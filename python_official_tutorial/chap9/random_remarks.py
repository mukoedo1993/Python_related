#If the same attribute name occurs in both an instance and in a class,
# then attribute lookup prioritizes the instance:
import sys

class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'

print(w2.purpose, w2.region)


# Function defined outside the class
def f1(self,x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self)->str:
        return 'hello world'

    h = g

c1 =C()
print(c1.f(12,23))
print(c1.g())
print(C.f(c1,sys.argv[1],sys.argv[2]))

##Bag####


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)
    
    def addtwice(self, x):
        self.add(x)
        self.add(x)

ob1 = Bag();ob2 = Bag()
ob1.add('13')
ob1.add('shdh')
for it in sys.argv:
    ob2.add(it)
for it in ob1.data:
    print(it, end= '!')
    print('')

for it1 in ob2.data:
    if it1 not in ob1.data:
        print(it1,end=',')
        print('')


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$  python random_remarks.py 123 -236 13
storage west
storage east
12
hello world
123
13!
shdh!
random_remarks.py,
123,
-236,
"""