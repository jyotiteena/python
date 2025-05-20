import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6],[2,3,4]])

print("Array:\n", arr)
print("ndim:", arr.ndim)          # 2
print("shape:", arr.shape)        # (2, 3)
print("size:", arr.size)          # 6
print("dtype:", arr.dtype)        # int64 (depends on platform)
print("itemsize:", arr.itemsize)  # e.g., 8 bytes
print("nbytes:", arr.nbytes)      # 48 (itemsize * size)
print("transpose:\n", arr.T)      # 3x2 array
print(arr.data) # Memory buffer containing the actual elements (rarely used directly)
print(arr.flags) #	Info about memory layout (contiguity, alignment, etc.)