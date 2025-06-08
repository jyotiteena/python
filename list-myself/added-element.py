# using append, extend and insert 

# append and extend both added at last index 
# insert added at specified index number

emptyList = []

# only single element can added
emptyList.append("jyoti")
emptyList.append(["jyoti","test2"]) 
print(emptyList) # both data at same index , ['jyoti', ['jyoti', 'test2']]

# multiple element wants to added then using extend
emptyList.extend(["jingar","teena"])  
print(emptyList) # ['jyoti', ['jyoti', 'test2'], 'jingar', 'teena']

emptyList.insert(1,"final")
print(emptyList) #['jyoti', 'final', ['jyoti', 'test2'], 'jingar', 'teena']