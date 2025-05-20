# numpy.reshape(array, new_shape)
# # or
# array.reshape(new_shape)

import numpy as np

arr = np.array([1,2,3,4,5,6])

output1 = arr.reshape((2,3))
print(arr) #[1 2 3 4 5 6]
print(output1) # 2x3 matrix
# [
# [1 2 3]
# [4 5 6]
# ]

output2 = arr.reshape((3,2))
print(output2) # 3x2


random_val = np.arange(1,13)
output3 = random_val.reshape((4,3))
print(output3)

# Using -1 (Auto-calculate one dimension)
output4 = random_val.reshape((4,-1))
print(output4)