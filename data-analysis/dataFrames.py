import pandas as pd
list1 = [1,2,3,4]
output = pd.DataFrame(list1)
print(output)


# dict 
# unbalance data then show error 
# dict = {"name":["jyoti","teena"],"rank":[12,2,3]}
dict = {"name":["jyoti","teena","mega"],"rank":[12,2,3],"marks":[12,3,4]}
output2 = pd.DataFrame(dict)
print(output2)

# ////////// output ////////
# name and rank is column 
#     name  rank
# 0  jyoti    12
# 1  teena     2
# 2   mega     3

# if want to perticular column 

output3 = pd.DataFrame(dict, columns=["name"])
print(output3)

# multiple choose column
output3 = pd.DataFrame(dict, columns=["name","marks"],index=["A","B","C"])
print(output3)

#     name  marks
# A  jyoti     12
# B  teena      3
# C   mega      4

# perticular element get -> variable([columnName][index number])
print(output2["rank"][2]) #3


# dict with series 
dict2 = {"name":pd.Series(["jyoti","teena"]),"id":pd.Series([123,444])}
outupt4 = pd.DataFrame(dict2)
print("outupt4............")
print(outupt4)

#   name   id
# 0  jyoti  123
# 1  teena  444