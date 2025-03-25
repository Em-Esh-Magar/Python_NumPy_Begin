import numpy as np

a = np.array(22)  # --> Zero dimensional array
print(a)
        
        
# sort function   
a = np.array([5,3,6,7,2])
print(np.sort(a))


# contatenate two array:
b = np.array([9,6,7,5,3])
c = np.concatenate((a,b))
print(c)


# contatenate on 2D arrays:
ab = np.array([[1,2,3],[4,5,6]])
bc = np.array([[3,6,9]])

# on row
cd = np.concatenate((ab,bc),axis = 0)
print(cd)

# on column
de = np.array([[10],[11]])
print(np.concatenate((ab,de),axis=1))



# reshape concept:
a = np.array([1,2,3,4,5,6,7,8,9])
print(a.reshape(3,3))

ef = ab.reshape(1,6)
print(ef)


# Condition in an array
print(a[a>5])

a = np.array([[1,2,3],[4,5,6],[7,8,9,]])
data = a %2 == 0
print(data)



#  creating a new array with existing array
a = np.array([1,2,3,4,5,6,7,8,9])
b = a[3:8]      # From 3rd index to 7th index. 8th index is not included
print(b)


# vstack and hstack of 2d arrays:
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.vstack((a,b))
print(c)

c = np.hstack((a,b))
print(c)


# Basic array operations  --> addition, subtraction, multiplication and division
print(a+b)
print(a-b)
print(a*b)
print(a/b)



# 2D array slicing
a = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
print(a[1:4])
print(a.max())
print(a.min())
print(a.sum())


b = np.array([[1,1]])
c = a+b     # --> is possible due to concept of broadcasting
print(c)



# Random number generator
rng = np.random.default_rng()
data = rng.random((3,2))
print(data)
data = rng.random(5)
print(data)


# unique data
a = np.array([ [[1,2,3],[4,2,7]], [[4,5,6],[6,7,8]] ])   # #D array using 2D array
print(a.ndim)
print(np.unique(a))