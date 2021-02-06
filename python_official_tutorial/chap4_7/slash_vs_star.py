"""
A function might look like:
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only

"""



def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)

def combined_example(pos_only,/, standard,*,kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)#2
standard_arg(arg=2)#2

pos_only_arg(2)#2
#pos_only_arg(arg=2)
"""
Traceback (most recent call last):
  File "slash_vs_star.py", line 30, in <module>
    pos_only_arg(arg=2)
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
"""
kwd_only_arg(arg = 2)#2

#kwd_only_arg(2)

"""
Traceback (most recent call last):
  File "slash_vs_star.py", line 39, in <module>
    kwd_only_arg(2)
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
"""

#combined_example(1,2,3)
"""
Traceback (most recent call last):
  File "slash_vs_star.py", line 48, in <module>
    combined_example(1,2,3)
TypeError: combined_example() takes 2 positional arguments but 3 were given
"""

#combined_example(pos_only=1, standard=2, kwd_only=3)
"""
Traceback (most recent call last):
  File "slash_vs_star.py", line 56, in <module>
    combined_example(pos_only=1, standard=2, kwd_only=3)
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
"""

combined_example(1, 2, kwd_only=3)#1 2 3

combined_example(1, standard=2, kwd_only=3)#1 2 3