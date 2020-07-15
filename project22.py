from array import *


vals=array('i',[5,6,3,5,34,23,3,23,2,23,22])

print(vals)

vals.reverse()
print(vals)

vals.append(56)
print(vals)

for i in vals:
    print(i)

print()

for i in range(len(vals)):
    print(vals[i])

print()

newArr= array(vals.typecode, ( a for a in vals))

print(newArr)
print()

for i in newArr:
    print(i)

print()

newArr= array(vals.typecode, ( a*a for a in vals))
print(newArr)

print(sorted(newArr))

print()





