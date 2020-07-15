

from numpy import *

arr1= array([1,2,3,4,5])
arr2= array([6,7,8,9,10])
print(sin(arr1))
print(sum(arr1))

arr3= arr1 + arr2
print(arr3)

arr1=arr1+5
print(arr1)

print(concatenate([arr1,arr2]))


for i in range(0,len(arr1)):
    arr1[i]=arr1[i]+5
print(arr1)




arr= empty(5)
for i in range(0,len(arr1)):
    arr[i]=arr1[i]+arr2[i]
print(arr)

#Max without in-built function

arr=array([1,5,7,2,4,67,27,23,21])
max=0
#or max=arr[0]
for i in arr:
    if i>max:
        max=i

print(max)

from array import *
arr = array('i',[1,2,3,4,5])
arr1 = array('i',[])


for i in range(len(arr)):
    arr1.append(arr[i]+5)
print(arr1)
































