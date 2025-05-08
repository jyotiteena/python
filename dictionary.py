 # pair format
#  key and value 
# unordered, mutable, don't allow duplicate key 

dict = {
    "name":"jyoti",
    "id":56,
    "marks":[1,2,3],
    "tuple1":(11,12,13),
    123:23,
    ("test",):76767
}
print(dict)
print(dict['name'])
print(dict["marks"])

# override
dict["id"] = 1001

# new key and value pair added
dict["final"] = "world"
print(dict)

# empty dict
empty_dict = {}
print(empty_dict)
print(type(empty_dict))