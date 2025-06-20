dict1 = {"name":"jyoti",'grid':2333}
print(dict1)
print(dict1.values())

print(dict1.keys())

print(dict1.items()) #[('name', 'jyoti'), ('grid', 2333)])

print(dict1.get('name')) # jyoti

print(dict1.get('phone')) # None
dict1.pop('grid')

print(dict1)

dict1.update({'age':34,'grid':322}) # add key value

print(dict1)

dict1.popitem() # remove last key
print(dict1) #{'name': 'jyoti', 'age': 34}