import pandas as pd
data = [12,3,4,5,66]
a = pd.Series(data)
print(a)

print(a[2]) # 4

# ////////////// answer ///////////////
# 0    12
# 1     3
# 2     4
# 3     5
# 4    66
# dtype: int64

# can be change index numbers 
b = pd.Series(data,index=["A","B","C","D","E"])
print(b)

# ///////// answer ///////

# A    12
# B     3
# C     4
# D     5
# E    66

# can be change data type  - > all values as a float
c = pd.Series(data,index=["A","B","C","D","E"],dtype="float")
print(c)

# ////// name of data 
c = pd.Series(data,index=["A","B","C","D","E"],dtype="float",name="list data")
print(c)

# /////// answer ///////
# Name: list data, dtype: float64
