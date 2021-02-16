import json
json.dumps([1,'simple','list'])

f=open('workfile_json','r+')

x = {12:'nima',13:27}

json.dump(x,f)
json.dump(x,f)
json.dump(x,f)

