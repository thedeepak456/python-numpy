# Copy and view


# copy made changes in a new array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
# x = arr.view()
arr[0] = 42

print(arr)
print(x)
