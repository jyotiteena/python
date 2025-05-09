obj = {
    "id":123,
    "name":"jyoti",
    "address":{
        "city":"jodhpur",
        "state":"rajasthan"
    }
}
# ////// all keys ///
print(obj.keys())

# ////// all values ///
print(obj.values())


# get value with list format
print(list(obj.values()))
print(list(obj.keys()))


# items  -> convert into key and values pair a a tuple
print(obj.items())

pairs = list(obj.items())
# singleValue = pairs[0]
# singleValue = pairs[1]
singleValue = pairs[2]
print(singleValue)


# //// diff b/w dict["key"] and dict.get("key")
# if key not exist then error in dict["key "] and next program stop
# if key not exist then None in dict.get("key") and also work next program


# print(obj["id2"])
print(obj.get("id2")) # None
print("final coding............") 

# output 
# None
# final coding............

# /////// update(newdict)  ////////
# insert the specified  item to dictionary 

new_dict = {"grid":2333}
obj.update(new_dict)
print(obj)

obj["address"].update(new_dict)
print(obj)
