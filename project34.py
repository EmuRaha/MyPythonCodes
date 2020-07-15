


#factorial

def fact(n):

   if n==0:
      return 1


   f=n*fact(n-1)
   return f


#fibonacci

def fibo(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fibo(n-1)+fibo(n-2)



num={}

def fibo1(n):
   if n==0:
      return 0
   elif n==1:
      return 1

   if n in num:
      return num[n]

   else:
      f = fibo1(n-1)+fibo1(n-2)
      num[n]=f
      return f



print(fibo1(100))

















