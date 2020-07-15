
n=int(input("number of rows="))



for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="  ")
    for k in range(i,0,-1):
        if k<=9:
            print(k, end="  ")
        else:
            print(k, end=" ")
    for l in range(i-1):
        if l+2<=8:
            print(l+2, end="  ")
        else:
            print(l+2, end=" ")
    print()
print()

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="  ")
    for k in range(i,0,-1):
        if k<=9:
            print(k, end="  ")
        else:
            print(k, end=" ")
    for l in range(2,i+1):
        if l<=8:
            print(l, end="  ")
        else:
            print(l, end=" ")
    print()

print()
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="  ")
    for k in range(i,0,-1):
        if k<=9:
            print(k, end="  ")
        else:
            print(k, end=" ")
    for l in range(i-1):
        if l+2<=8:
            print(l+2, end="  ")
        else:
            print(l+2, end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="  ")
    for k in range(i,0,-1):
        if k<=9:
            print(k, end="  ")
        else:
            print(k, end=" ")
    for l in range(2,i+1):
        if l<=8:
            print(l, end="  ")
        else:
            print(l, end=" ")
    print()

print()





















