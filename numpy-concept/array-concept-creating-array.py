# zeros(), ones(), empty(), and arange()

# /////// zeros //////
import numpy as np

# 1D array of zeros
zeros_1d = np.zeros(5) # [0. 0. 0. 0. 0.]

# 2D array of zeros
zeros_2d = np.zeros((2, 3))

print("zeros_1d:\n", zeros_1d)
print("zeros_2d:\n", zeros_2d)

#[[0. 0. 0.]
#[0. 0. 0.]]

# ///// ones ////////////

ones_1d = np.ones(4) #[1. 1. 1. 1.]

# 2D array of ones
ones_2d = np.ones((2, 2)) 

print("ones_1d:\n", ones_1d)
print("ones_2d:\n", ones_2d)

#  [[1. 1.]
#  [1. 1.]]

# ///// empty ////////////

# empty - the values are random garbage (whatever is in memory).
# 1D empty array
empty_1d = np.empty(3)

# 2D empty array
empty_2d = np.empty((2, 3))

print("empty_1d:\n", empty_1d)
print("empty_2d:\n", empty_2d)

# ///// arange ////////////

# From 0 to 9
range1 = np.arange(10)

# From 1 to 20 with step 2
range2 = np.arange(1, 20, 2)

print("range1:\n", range1)
print("range2:\n", range2)


