# sum 
import pandas as pd
dict = pd.DataFrame({"A":[2,4,6,8], "B":[1,2,3,4]})
print(dict)

# //////// sum of list  
dict["C"] = dict["A"] + dict["B"]
print(dict)
#    A  B  C
# 0  1  1  2
# 1  2  2  4
# 2  3  3  6
# 3  4  4  8

print()
dict["C"] = dict["A"] - dict["B"]
print(dict)

# operations = +, -, *, / 

# filtering according to conditions 
