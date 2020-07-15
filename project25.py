


from array import *

# Write a code to reverse an array without using in-built functions.

vals=array('i',[5,6,3,5,34,23,3,23,2,23,22])
new= array('i',[])
for i in range(len(vals)-1,-1,-1):
    p=vals[i]
    new.append(p)
print(new)

#Create an array with 5 values and delete the value at index number 2 without using in-built functions.
new2=array('i',[])
for i in range(0,len(vals)):
    if i==2:
        continue

    new2.append(vals[i])
print(new2)
#(or)Create an array with 5 values and delete the value at index number 2 without using in-built functions.
new2=array('i',[])
new2=array('i',[])
for i in range(0,len(vals)):
    if i!=2:
        new2.append(vals[i])
print(new2)


























