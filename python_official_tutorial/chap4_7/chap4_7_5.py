#Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a
# list or tuple but need to be unpacked for a function call requiring
# separate start and stop arguments. If they're not available separately, 
# write the function call with the *-operator to unpack the arguments out of a list
#or a tuple:

print(list(range(3,6)))
args=[3,6]

print(list(range(*args)))


#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
def parrot(volt, state='a stiff', action='voom'):
    print("nimas",action,end=' ')
    print("if you put", volt, "volts through it.", end= ' ')
    print("E's",state,"!")

d={"volt":"four million", "state":"bleeding' demise","action":"chenqian"}
parrot(**d)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python chap4_7_5.py
[3, 4, 5]
[3, 4, 5]
nimas chenqian if you put four million volts through it. E's bleeding' demise !
"""