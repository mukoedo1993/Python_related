f = open('workfile3', 'rb+')#Before the operation, the workfile3 is a blank txt file.
f.write(b'0123456789abcdef')



"""
To change the file object's position, use f.seek(offset, whence).
The position is computed from adding offset to a reference point;
the reference point is selected by the whence argument. A whence
value of 0 measures from the beginning of the file, 1 uses the curren
"""
print(f.seek(5))   #Go to the 6th byte in the file

print(f.read(1)) #read or write until n bytes. If negative or none, then to EOF

print(f.seek(-3, 2))   #Go to the 3rd byte before the end

print(f.read(1))

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_2$ python seek_and_read.py
5
b'5'
13
b'd'
"""