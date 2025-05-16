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
dict["A>4"] = dict["A"]>4
dict["B<4"] = dict["B"]<4
print(dict)

#    A  B  C    A>4    B<4
# 0  2  1  1  False   True
# 1  4  2  2  False   True
# 2  6  3  3   True   True
# 3  8  4  4   True  False

