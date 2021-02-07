"""
It is also possible to use a list as a queue, where first element added is 
the first element retrived (FIFO); however, lists are not
efficient for this purpose. While appends and pops from the end of list are
fase, doing inserts or pops from the beginning of a list is slow (because
all of the other elements have to be shifted by one). 

To implement a queue, 
"""

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")

queue.append('Graham')

queue.popleft();queue.popleft()

print(queue)

queue.appendleft("Edward")
queue.appendleft("Rice")
print(queue)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_1$ python list_as_queue.py
deque(['Michael', 'Terry', 'Graham'])
deque(['Rice', 'Edward', 'Michael', 'Terry', 'Graham'])
"""