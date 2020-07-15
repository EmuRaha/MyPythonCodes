

from numpy import *

arr1 = array([
              [1,2,3,4],
              [5,6,7,8],
              [3,5,7,2]


              ])



print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print()
arr2=arr1.flatten()
print(arr2)
print()
arr3= arr1.reshape(6,2)
print(arr3)
print()
arr4= arr1.reshape(2,2,3)
print(arr4)
print()
#Matrix

m= matrix(arr1) #converting array to matrix
print(m)
print()
#creating marix

m1= matrix('1 2 3; 4 5 6; 7 8 9')
m2= matrix('1 2 3; 4 5 6; 7 8 9')
print(m1)
print(m2)
print()
m3= m1 + m2
print(m3)
print()
m4= m1 * m2
print(m4)
#multiplication operation without in built function