
from numpy import *

a1=int(input('number of rows='))
b1=int(input('number of columns='))

n1=a1*b1
A=matrix(zeros(n1,int).reshape(a1,b1))

for i in range(a1):
    for j in range(b1):
        x=int(input('enter value='))
        A[i,j]=x
print('matrix A is:')
print(A)

a2=int(input('number of rows='))
b2=int(input('number of columns='))

n2=a2*b2
B=matrix(zeros(n2,int).reshape(a2,b2))

for i in range(a2):
    for j in range(b2):
        x=int(input('enter value='))
        B[i,j]=x
print('matrix B is:')
print(B)

n3=a1*b2
C=matrix(zeros(n3,int).reshape(a1,b2))

if b1==a1:
    n=b1=a2
    for i in range(a1):
        for j in range(b2):
            x=0
            for k in range(n):
                x=x+A[i,k]*B[k,j]
            C[i,j]=x
    print('miltiplication is:')
    print(C)
else:
    print('multiplication not possible')
