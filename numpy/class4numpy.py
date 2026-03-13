# Dimensions in numpy array

import numpy as np

arr1 = np.array([1,2,3,4,5]) # one dimensions
arr2 = np.array(  [ [1,2,3],[4,5,6] ]  )  # two dimensions
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # three dimensions

print(arr1)
print(arr2)
print(arr3)

# To check the dimensions of numpy array we use (ndim)

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)



# if we want the custom dimension in our array we can use (ndmin)

arr4 = np.array([1,2,3,4,5,6,7,8,9,10], ndmin=5)

print(arr4)
print(arr4.ndim)