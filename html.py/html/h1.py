import json
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
print(type(x))
print("x=",x)
try:
 print(x["age"])
except:
 print("ocorreu um erro")
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print(type(y))
print("y=",y)
