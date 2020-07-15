
str=input("enter a word/sentence/whatever the fuck you want=")

n=len(str)

for x in range(n):
    for i in range(len(str)):
        for j in range(i+1):
            print(str[j],end="")
        print()
    print()

    for i in range(n):
        for j in range(n-i):
            print(str[j],end="")
        print()
    print()

