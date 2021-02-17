#The use of the else clause is better than adding additional code
# to the try clause because it avoids accidentally
#catching an exception that wasn't raised by the code
#being protected by the try ... except statement.

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except OSError:
        print('cannot open', arg)
    else:#Else must follow all except:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()



"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python else.py
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python else.py sdhfh
cannot open sdhfh
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python else.py myfile.txt
myfile.txt has 3 lines
"""