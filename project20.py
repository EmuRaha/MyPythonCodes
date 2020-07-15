

n=int(input("Rows="))


for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(i):
        print(end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()
print()

for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(i):
        print(end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()
print()
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
print()

for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
print()


for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i):
        print(i,end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(end=" ")
    for k in range(i):
        print(i,end=" ")
    print()
print()
