import numpy as np
import math

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.shape)          # Returns the row * column size
print(f"The dimensional = {a.ndim}")
print(a,type(a))


# list is passed 
# for i in a:
#     print(i)


# 1-D Array
a = np.array([1,2,3,4,5,6,7,8])
print(a)

a[0] = 10
print(a)

print(f"The dimensional = {a.ndim}")
# print(a[:3])
# print(a[3:])


b = len(a.shape)
print(b)

# The length of ndarray is equals to the dimentsion of an array
if b == a.ndim:
    print(True)
    
print(f"The size is : {a.size}")
print(f"The size is : {len(a)}")

if a.size == math.prod(a.shape):
    print(True)
    
    
# creating array using ones and zeros 
ab = np.zeros(4)
print(ab)
ab = np.ones(2)
print(ab)

# creating array using empty
ab = np.empty(3)
print(ab)



# creating array using arange
ab = np.arange(3)
print(ab)


ab = np.arange(0,10,3)
print(ab)


ab = np.arange(0,10)
print(ab)


# Creating using linespace
ab = np.linspace(0,10,num=6)
print(ab)
