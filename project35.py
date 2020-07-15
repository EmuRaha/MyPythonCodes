

#anonymus function

f = lambda a : a*a

print(f(5))

f = lambda a,b : a+b

print(f(5,6))

#filter

def even(n):
    return n%2==0



lst=[1,2,3,4,5,6,7,8,9,10]

evens= list(filter(even,lst))
print(evens)

#using lambda
#filter

lst=[1,2,3,4,5,6,7,8,9,10]

evens= list(filter(lambda n : n%2==0,lst))
print(evens)


#map(doesn't filter, takes a value, runs the operation)

doubles= list(map(lambda n : n*2,evens))
print(doubles)

#reduce(gives only one value)

from functools import reduce


sum= reduce(lambda a,b : a+b, doubles)
print(sum)






























































