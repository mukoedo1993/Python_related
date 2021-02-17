bookmark: すべての　CHAP9 unread


https://docs.python.org/3/tutorial/

https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

Python never implicitly copies objects. When you set dict2 = dict1, you are making them refer to the same exact dict object, so when you mutate it, all references to it keep referring to the object in its current state.

If you want to copy the dict (which is rare), you have to do so explicitly with

dict2 = dict(dict1)
or

dict2 = dict1.copy()
