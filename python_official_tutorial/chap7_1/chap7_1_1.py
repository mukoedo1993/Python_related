"""
So far we've encountered two ways of writing values:
expressiong statements and the print() function. 
(A third way is using the write() method of file objects;
the std. output file can be referenced as sys.stdout.
See the Lib. Ref. for more information on this.)
"""

"""
To use formatted string literals, bring a string with f or F
before the opening quotation mark or triple quotation mark.
Inside this string, you can write a Python expression between
{ and } characters that can refer to variables or literal values.
"""

year = 2016
event = 'Referendum'
tmp1 = f'Results of the {year} {event}'
print(tmp1)


"""
The str.format():
"""

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes,percentage))

"""
Result:
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_1$ python chap7_1_1.py
Results of the 2016 Referendum
 42572654 YES votes 49.67%
"""