"""
We saw that lists and strings have many
common properties, such as indexing and 
slicing operations. They are two examples
of sequence data types (see Sequence Types --
list, tuple, range). Since Python is an evolving
language, other sequence data types may be added.
There is also another std. sequence data type: the tuple.
"""


"""
Though tuples may seem similar to lists, they are often
used in different situations and for different purposes. Tuples 
are immutable, and usu. contain a heterogeneous sequence of elements
that are accessed via unpacking (see later in this section) or indexing
(or even by attribute in the case of namedtuples). Lists are mutable, and 
their elements are usu. homogeneous and are accessed by iterating over the list.
"""


"""
A speical problem is the construction of tuples containing 0 or 1 items:
the syntax has some extra quirks to accomodate these. Empty tuples
are constructed by an empty pair of parentheses; 
a tuple with one item is constructed by following a value with a comma
(it is not sufficient to enclose a single value in parentheses). 
Ugly, but effective. For example: 
"""

t=(13,'shsh',"Zhongjing Liu")
empty = ()
singleton = 'hello',  # <-- note trailing comma
len(empty)

len(singleton)
print(empty)
print(singleton)

x,y,z=t
print(x)
print(y)
print(z)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_3$ python chap5_3_part2.py()
('hello',)
13
shsh
Zhongjing Liu
"""