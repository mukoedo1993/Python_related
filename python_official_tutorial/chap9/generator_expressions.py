print(sum(i*i for i in range(10)))

xvec = [10,20,30]
yvec = [7,5,3]
print(sum(x*y for x,y in zip(xvec,yvec)))


f = open ('words.txt','r')
unique_words = set(word for line in f  for word in line.split())    
print(unique_words)

class graduate:
    def __init__(self,name:str,gpa:float):
        self.name = name
        self.gpa = gpa
"""    
    def __lt__(self, other):
        return self.gpa < other.gpa

    def __le__(self, other):
        return self.gpa <= other.gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __ne__(self, other):
        return self.gpa != other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __ge__(self, other):
        return self.gpa >= other.gpa

    def __str__(self):
        return str(self.value)        
"""

graduates =[(graduate('str',3.41)),graduate('tom',3.25),graduate('hehe',3.76),graduate('Mukoto',3.75)]

valedictorian = max((students.gpa,students.name)for students in graduates)
print(valedictorian)

data = 'golf'

print(list(data[i] for i in range(len(data)-1,-1,-1)))


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python generator_expressions.py
285
260
{'no', 'standard', 'attribute', 'absolutely', 'for', 'however,', 'following', 'names', 'programmers,', 'first', 'relies', 'convention.', 'syntax', 'use', 'to', 'name', 'such', 'browser', 'Attribute', 'convention', 'were', 'self.', 'written', 'Python:', 'it', 'method', 'has', 'called', 'namespace', 'when', 'object', 'be', 'less', 'upon', 'in', 'code', "class's", 'convention:', 'may', 'than', 'meaning', 'readable', 'Note,', 'self', 'by', 'Valid', 'a', 'self:', 'of', 'not', 'that', 'also', 'program', 'Python', 'is', 'This', 'other', 'obj.name.', 'argument', 'might', 'created.', 'the', 'class', 'more', 'was', 'references', 'all', 'nothing', 'Often,', 'special', 'Python.', 'your', 'conceivable', 'are', 'and', 'used'}
(3.76, 'hehe')
['f', 'l', 'o', 'g']
"""