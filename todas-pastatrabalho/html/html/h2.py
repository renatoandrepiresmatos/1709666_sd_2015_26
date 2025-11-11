import json

fille_path='t1.json'
with open(fille_path,'r',encoding='utf-8) as f:
      data=json.load(f)


# the result is a Python dictionary:
print(data['0'])
print(data['0']['age'])
print(type(data))
print("data=", data)