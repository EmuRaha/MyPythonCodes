n=int(input("length="))

list=[]
for i in range(n):
    j=int(input('Enter number='))
    list.append(j)
print(list)

print()

from array import *

n=int(input("length="))

vals=array('i',[])

for i in range(n):
    p=int(input('Enter something according to the typecode='))
    vals.append(p)
print(vals)

num=int(input("Enter the number you're searching for="))

k=0
for e in vals:
    if e==num:
        print(k)
        break
    k=k+1

print(vals.index(num))




