matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

#The following list comprehension will transpose rows and columns:

#The outside for is executed first, then the inside for.
# i in range(4) is executed first, as the outer loop.  Then, for row in matrix is executed, as the inner loop. 
tmp1 = [[row[i] for row in matrix] for i in range(4)]
print(tmp1)


transposed = []
for i in range(4) :
    transposed.append([row[i] for row in matrix])

print(transposed)




transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

#In the real world, you should prefer built-in functions to
#complex flow statements. The great job for this use case:
tmp_yaju1 = list(zip(*matrix))
print(tmp_yaju1)
"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_1$ python nested_list_comprehensions.py
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
"""

