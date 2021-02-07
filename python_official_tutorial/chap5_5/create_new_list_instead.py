#Sometimes, it is simpler and safer to
#create a new list instead

import math
raw_data = [56.2, float('NaN'),51.7,55.3, 52.5, float('NaN'),47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

"""
(base) zcw@mukoedo1993:~/python_related_clone/Python_related/python_official_tutorial/chap5_5$ python create_new_list_instead.py
[56.2, 51.7, 55.3, 52.5, 47.8]
"""