# Method overloading

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        if a==None:
            a=0
        if b==None:
            b=0
        if c==None:
            c=0

        s=a+b+c
        return s

s1 = student(34,98)

print(s1.sum(2))

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

s1 = student(34,98)

print(s1.sum(2,3))

# Method overriding

class A:

    def show(self):
        print("in A show")

class B(A):
    pass

a = A()
a.show()
a=B()
a.show()
print()
class A:

    def show(self):
        print("in A show")

class B(A):

    def show(self):
        print("in B show")




a = A()
a.show()
a=B()
a.show()













































