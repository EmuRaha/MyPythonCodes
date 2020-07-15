# Polymorphism
# Operation-overloading


a = 5
b  = 6
print(a + b)
print(int.__add__(a,b))
print(a.__add__(b))


class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        return r1 > r2

    def __mul__(self, other):
        m1 = self.m1* other.m1
        m2 = self.m2*other.m2
        mul = student(m1,m2)
        return mul



s1 = student(34,98)
s2 = student(65,76)

s3 = s1 + s2
print(s3.m1,s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")



s3 = s1*s2

print(s3.m1,s3.m2)

a = 9
print(a)
print(s1)
print(s2)
print()
print(a.__str__())
print(s1.__str__())
print(s2.__str__())

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        return r1 > r2

    def __mul__(self, other):
        m1 = self.m1* other.m1
        m2 = self.m2*other.m2
        mul = student(m1,m2)
        return mul

    def __str__(self):
        return self.m1,self.m2
s1 = student(34,98)
s2 = student(65,76)

print()
a = 9
print(a)
print(a.__str__())
print(s1.__str__())
print(s2.__str__())
print()
print()


class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        return r1 > r2

    def __mul__(self, other):
        m1 = self.m1* other.m1
        m2 = self.m2*other.m2
        mul = student(m1,m2)
        return mul

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
s1 = student(34,98)
s2 = student(65,76)

print()
a = 9
print(a)
print(s1)
print(s2)
print(a.__str__())
print(s1.__str__())
print(s2.__str__())

















