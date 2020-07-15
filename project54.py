# Generator

def TopTen():

    yield 1
    yield 2
    yield 5
    yield 0

values = TopTen()

for i in values:
    print(i)
print()
print()

def Topten():

    n = 1
    while n<=10:
        yield n
        n +=1

values = Topten()

for i in values:
    print(i)


print()
print()



def Topten():

    n = 1
    while n<=10:
        yield n*n
        n +=1

values = Topten()

for i in values:
    print(i)








































