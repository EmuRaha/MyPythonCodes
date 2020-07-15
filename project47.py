#inheritence

class A:
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B(A):
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

class C(B):
    def feature5(self):
        print("Feature5 working")
    def feature6(self):
        print("Feature6 working")
print("For a1:")
a1 = A()
a1.feature1()
a1.feature2()
print()

print("For b1:")
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
print()

print("For c1:")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()
print()
class A:
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B:
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

class C(A,B):
    def feature5(self):
        print("Feature5 working")
    def feature6(self):
        print("Feature6 working")
print("For a1:")
a1 = A()
a1.feature1()
a1.feature2()
print()

print("For b1:")
b1 = B()
b1.feature3()
b1.feature4()
print()

print("For c1:")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()































