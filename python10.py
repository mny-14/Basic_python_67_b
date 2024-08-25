#
# Part: Python JSON
# API = Application Programming Interface
#



import json

# make a json (Dictionary stying)
x = '{"name" : "John" , "age" : 20 , "city" : "Phuket"}'
print(x)

# parse
y = json.loads(x)

# python Dictionary
print(y)
print(type(y))
print(y["city"])


#python di

a = {
    "name" : "Noa" ,
    "age" : 20 ,
    "city" : "Phuket"


}


#convert to JSON (string)
b = json.dumps(a)

# JSON String
print(b)


