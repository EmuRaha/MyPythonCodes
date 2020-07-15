

for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()

for i in range(5):
    for j in range(i):
        print("# ",end="")
    print()

print()

for i in range(4,0,-1):

    for j in range(i):
        print("# ",end="")
    print()

print()
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()
print()
for i in range(1,5):
    for j in range(i,5):
        print(j , end="")
    print()

print()

string = '1234'
for i in range(len(string)):
    print(string[i:])

print()
for i in range(1, 5):
    for j in range(1,6-i):
        print(j, end="")
    print()

print()
for i in range(1, 5):
    for j in range(1,6-i):
        print(i, end="")
    print()

print()


str1="ABCD"
str2="PQR"

for i in range(4):
    for j in range(i+1):
        print(str1[j], end="")
    for k in range(i,3):
        print(str2[k], end="")
    print()

print()
for i in range(4):

    print(str1[:i+1], end="")
    print(str2[i:3], end="")
    print()

print()


