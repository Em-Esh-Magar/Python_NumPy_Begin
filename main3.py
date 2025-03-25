import numpy as np

        
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