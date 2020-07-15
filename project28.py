

from numpy import *
#copy(same address)
arr1= array([1,4,23,45,12])

arr2=arr1

print(arr1)
print(arr2)


print(id(arr1))
print(id(arr2))
print()

#shallow copy(different address but dependent)
arr1= array([1,4,23,45,12])

arr2=arr1.view()

arr1[1]=42

print(arr1)
print(arr2)


print(id(arr1))
print(id(arr2))
print()

#deep copy(different address and not dependent)
arr1= array([1,4,23,45,12])

arr2=arr1.copy()

arr1[1]=42

print(arr1)
print(arr2)


print(id(arr1))
print(id(arr2))






































