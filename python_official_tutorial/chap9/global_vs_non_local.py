#The global statement can be used to indicate that particular
#variables live in the global scope and should be rebound there;
# the nonlocal statement indicates that particular variables live in
#in an enclosing scope and should be rebound there.
def scope_test() ->None:
    def do_local()->None:
        spam = "local spam"
    
    def do_nonlocal()->None:
        nonlocal spam
        spam = "nonlocal spam"

    def do_global()->None:
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("After local assignment:",spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:",spam)

scope_test()
print("In global scope:",spam)



"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap9$ python global_vs_non_local.py
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
"""