f = open('workfile1', 'r')
f1 = open('workfile2','r+')
print(f.readline())
print(f.readline())
print(f.readline())



for line in f:
    print(line, end=' ')

f1.write('This is a test\n')
value = ('the answer', 42)
s = str(value) #convert the tuple to a string
f1.write(s)
f1.close()
f1 = open('workfile2','r+')
for line1 in f1:
    print(line1, end=' ')

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap7_2$ python read_lines.py
test test

workfile1

if there is still a chance

fight 
 until the very end
 not surrender
 just fight
 against genocidal regime
 This is a test
 ('the answer', 42)This is a test
"""