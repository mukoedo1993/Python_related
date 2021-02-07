import copy

a = [-1, 1, 66.25, 333, 333, 1234.5];a1=copy.deepcopy(a);a2=copy.deepcopy(a);a3=copy.deepcopy(a)

del a[0];print(a)

del a1[2:4];print(a1)

del a2[:];print(a2)

del a3#; print(a3)
"""
Reference to a3 hereafter is an error(at least until other value is assigned to it.)

"""