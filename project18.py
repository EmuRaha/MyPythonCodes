

n=int(input("number of rows="))

for i in range(1,n+1):
    d=n-1
    for j in range(i):
        if i<=9:
            print(i,end="  ")
        else:
            print(i, end=" ")
        i=i+d
        d=d-1

    print()


