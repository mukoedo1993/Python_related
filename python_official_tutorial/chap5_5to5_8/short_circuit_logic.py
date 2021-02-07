"""
The Boolean operators and and or are so-called short-circuit
operators: their arguments are evaluated from left to right, and evaluation
stops as soon as the outcome is determined. For example, if A and C are true
but B is false, A and B and C does not evaluate the expression C. When used as a general value
and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.
"""

string1, string2, string3 ='','Trondheim', 'Hammer Dance'
not_null = string1 or string2 or string3

print(not_null)

all_null = string2 and string3

print(all_null)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_5to5_8$  python short_circuit_logic.py
Trondheim
Hammer Dance
"""