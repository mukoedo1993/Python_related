def ask_ok(prompt, retries=4, reminder= 'Please try again!'):
	while True:
		ok = input(prompt)
		if ok in('y','ye','yes'):
		 return True
		if ok in('n','no','nop','nope'):
		 return False
		retries = retries - 1
		if retries <0:
		 raise ValueError('invalid user response')
		print(reminder)


ask_ok("do you really want to quit?")

ask_ok("Ok to overwrite the file?",2)

ask_ok("OK to overwrite the file? ",2,"come on, only yes or no!")


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python ask_ok.py
do you really want to quit?ha
Please try again!
do you really want to quit?h
Please try again!
do you really want to quit?ha
Please try again!
do you really want to quit?ha
Please try again!
do you really want to quit?ha
Traceback (most recent call last):
  File "ask_ok.py", line 14, in <module>
    ask_ok("do you really want to quit?")
  File "ask_ok.py", line 10, in ask_ok
    raise ValueError('invalid user response')
ValueError: invalid user response
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap4_7$ python ask_ok.py
do you really want to quit?ye
Ok to overwrite the file?nope
OK to overwrite the file? hehe
come on, only yes or no!
OK to overwrite the file? he
come on, only yes or no!
OK to overwrite the file? nope
"""