# When looping through dictionaries, the key and corresponding value
# can be retrieved at the same thing using items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print (k,v)

#When looping through a sequence, the position index and corresponding
#value can be retrieved at the same time using the enumerate() function.

for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

#To loop over two or more sequences at the same time, the entries
# can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot','the holy grail', 'blue']
for q,a in zip(questions,answers):
    print('what is your {0}? It is {1}'.format(q,a))

#To loop over a sequence in reverse, first specify the sequence in 
#a forward direction and then call the reversed() function.

for i in reversed(range(1,10,2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


# Using set() on a sequence eliminates duplicate elements. The use of
# sorted() in combination with set() over a sequence is an idiomatic way
# to loop over unique elements of the sequence in sorted order.

for i in sorted(set(basket)):
    print(i)


"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_5$ python chap5_6.py
gallahad the pure
robin the brave
0 tic
1 tac
2 toe
what is your name? It is lancelot
what is your quest? It is the holy grail
what is your favorite color? It is blue
"""