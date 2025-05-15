import pandas as pd
dict = {"name":["jyoti","teena"],"rank":[12,2,3]}
output = pd.Series(dict)
print(output)

# //////// answer ////////
# name    [jyoti, teena]
# rank        [12, 2, 3]
# dtype: object - because of mix data


# single data also can be added

output2 = pd.Series(12)
print(output2)

#0    12


# same data on all index 

output3 = pd.Series(12, index=[1,2,3,4])
print(output3)


# ///////// answer ///////
# 0    12
# 1    12
# 2    12
# 3    12
# 4    12
# dtype: int64
output4 = pd.Series(11,[1,2])
print(output3 + output4)
# 1    23.0
# 2    23.0
# 3     NaN
# 4     NaN
# dtype: float64

dict2 = {"name":["jyoti","teena","mega","neha"],"rank":[12,2,32,4]}
output5 = pd.DataFrame(dict2)




