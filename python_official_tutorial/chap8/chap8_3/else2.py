import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OS error: {0}.format(err)")
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error: ",sys.exc_info()[0])
    raise
    #(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_3$ python else2.py heheda
    #(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python