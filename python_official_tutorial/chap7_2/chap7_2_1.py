f = open('workfile', 'r')
print(f.read())

"""
The first argument is a string containing the filename.
The second argument is another string containing a few
characters describing the way in which the file will be used.
mode can be 'r' when the file will only be read, 'w' for
only writing(an existing file with the same file will be erased),
and 'a' opens the file for appending; any data written to the file
is automatically added to the end. 'r+' opens the file for both reading
and writing. The mode argument is optional; 'r' will be assumed if it's omitted.

"""


with open('workfile') as f1:#It is good practice 
    read_data = f1.read()

# We can check that the file has been automatically closed
print(f1.closed)

#Warning Calling 
# f.write() without using the with keyword or calling f.close() might result in the arguments of f.write() not being completely written to the disk, even if the program exits successfully.

f1.close()
f1.read()

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_2$ python chap7_2_1.py
test test!
for chap7_2
True
Traceback (most recent call last):
  File "chap7_2_1.py", line 27, in <module>
    f1.read()
ValueError: I/O operation on closed file.
"""