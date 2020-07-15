
n= int(input("Entar Number="))



for j in range(1,n+1):
    f=1
    for i in range(1,j+1):
        f=f*i
    print("Factorial of", j, "is", f)



n=int(input('n='))

f=1
for i in range(n-1,0,-1):
    f=n*i
    n=f

print(f)




