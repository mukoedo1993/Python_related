def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc
"""
base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap8/chap8_5$ python transforming_errors.pyon_related/python_official_tutorial/chap8/chap8_Traceback (most recent call last):
  File "transforming_errors.py", line 5, in <module>
    func()
  File "transforming_errors.py", line 2, in func
    raise IOError
OSError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "transforming_errors.py", line 7, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database
"""