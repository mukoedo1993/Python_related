squares = []; square1=[]; suqare2=[]
for x in range(10):
    squares.append(x**2)

print(squares)


#Note that this creates (or overwrites) a variable
#named x that still exists after the loop completes.
#We can calculate the list of squares without any
#side effects using:

square1 = list(map(lambda x:x**2, range(10)))

#or equivalently,
square2 = [x**2 for x in range(10)]

print("square1 is: ",square1)

print("square2 is: ",square2)


tmp3= [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(tmp3)

combs=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print(combs)


vec = [-4, -2, 0, 2, 4]

#create a new list with the values doubled
print([x*2 for x in vec])

#filter the list to exclude negative numbers
print([x for x in vec if x>=0])

# apply a function to all the elements
print([abs(x) for x in vec])


# call a method on each element
freshfruit = [' banana',' loganberry ','passion fruit ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
#print([x, x**2 for x in range(6)])
"""
  File "list_comprehension.py", line 54
    print([x, x**2 for x in range(6)])
                   ^
SyntaxError: invalid syntax
"""

#flatten a list using a listcomp with two 'for'
vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
tmp_yaju= [str(round(pi,i)) for i in range(1,6)]
print(tmp_yaju)



"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_1$ python list_comprehension.py
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
square1 is:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
square2 is:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
[-8, -4, 0, 4, 8]
[0, 2, 4]
[4, 2, 0, 2, 4]
['banana', 'loganberry', 'passion fruit']
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
"""