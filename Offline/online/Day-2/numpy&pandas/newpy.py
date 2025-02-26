import numpy as np
# data=[23,14,56,72,90]
# np.mean(data)
# np.float64(51.0)

# a=[1,2,3,5,6]
# b=[5,7,2,6,8]
# arr1= np.array(a)
# arr2=np.array(b)
# print(arr1*arr2)

# print(arr1.dtype)
# arr3= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr3.ndim)
# print(arr3.shape)
# print(np.arange(10,1,-1))

data4=np.random.randint(10,100,12).reshape(4,3)
data4.sort()
print(data4)