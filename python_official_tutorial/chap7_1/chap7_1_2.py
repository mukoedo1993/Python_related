print('we are the {} who say "{}!"'.format('knights','Ni'))


#positional argument in 0,1,..., et cetera.
print('{0} and {1}'.format('spam','eggs'))
print('{1} and {0}'.format('spam','eggs'))


#keyword arguments
print('This {food} is {adjective}.'.format(
    food = 'spam', adjective = 'absolutely horrible'
))

#Positional and keyword can be arbitraily combined
print('The story of {0}, {1}, and {other}'
.format('Bill', 'Manfred', 
       other='Georg'))

#If you have a really long format string that you don't
#want to split up, it would be nice if you could reference
#the variables to be formatted by name instead of by position.
# This can be done by simply passing the dict and using square
# brackets '[]' to access the keys.

table = {'Sjoerd': 4127, 'Jack':4098,'Dcab':8637678}
print('Jack:{0[Jack]:d}; Sjoerd: {0[Sjoerd]:d};Dcab: {0[Dcab]:d}'.format(table))

#This could also be done by passing the table as keyword arguments with the '**' notation.
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))



for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# There is another method, str.zfill(), which pads a numeric string on the left
# with zeros. It understands about plus and minus signs:
print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))


#Old string formatting
import math
print('The value of pi is approximately %5.3f. ' %math.pi)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_1$ python chap7_1_2.pywe are the knights who say "Ni!"
spam and eggs
eggs and spam
This spam is absolutely horrible.
The story of Bill, Manfred, and Georg
Jack:4098; Sjoerd: 4127;Dcab: 8637678
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
00012
-003.14
3.14159265359
The value of pi is approximately 3.142.
"""