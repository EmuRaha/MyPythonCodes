

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
r1,r2=add_sub(5,5)
r=add_sub(4,5)
print(r1,r2)
print(r)

def add_multiple_numbers(a,* b):

    x=a

    for i in b:
        x=x+i
    print('summation of multiple numbers is=',x)
add_multiple_numbers(15,20,30,40)

def add_multiple_numbers(a,* b):

    x=a+sum(b)


    print('summation of multiple numbers is=',x)
add_multiple_numbers(15,20,30,40)

def add_multiple_numbers(* a):

    x=sum(a)


    print('summation of multiple numbers is=',x)
add_multiple_numbers(15,20,30,40)







def area(r):
    from math import pi

    area= pi*r*r
    print('area of the circle is=',area)

area(1.2)

print()

def update(x):

    x=8

    print(x)
    print(id(x))
    print(a)
    print(id(a))
a=10
print(a)
print(id(a))

update(a)

print()

def update(x):

    x[1]=15

    print(x)
    print(id(x))
    print(a)
    print(id(a))
a=[10,20,30]
print(a)
print(id(a))

update(a)

print()
#Keyworded Variable Length Arguments

def person(name, **data):

    print(name)
    print(data)

    for i,j in data.keys(),data.values():
        print(i,j)

    for i, j in data.items():      #or
        print(i, j)


person('Emu',age=20,city='dhaka')

print()


#Global Keyword

a=10

def A():

    a=15  #local variable

    print('in func',a)
    print(id(a))
A()

print('outside',a)
print(id(a))

print()

a = 10


def A():
    global a
    a = 15  # global variable

    print('in func', a)
    print(id(a))


A()

print('outside', a)
print(id(a))

print()

a = 10


def A():

    a = 15  # local variable

    x=globals()['a']   #global

    print('in func', a)
    print('id a',id(a))
    print('x', x)
    print('x id', id(x))


A()

print('outside', a)
print(id(a))


print()

a = 10


def A():

    a = 15  # local variable

    x=globals()['a']=30  #global

    print('in func', a)
    print('id a',id(a))
    print('x', x)
    print('x id', id(x))


A()

print('outside', a)
print(id(a))


















