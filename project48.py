
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B(A):
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")


a1 = A()
b1 = B()
print()


class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B(A):

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")


a1 = A()
b1 = B()
print()


class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B(A):

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

b1 = B()
print()

class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B:

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

class C(A,B):
    def feature5(self):
        print("Feature5 working")
    def feature6(self):
        print("Feature6 working")

c1 = C()
print()
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")

class B:

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")

class C(A,B):

    def __init__(self):
        print("in C init")

    def feature5(self):
        print("Feature5 working")
    def feature6(self):
        print("Feature6 working")

c1 = C()
print()
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1-A working")
    def feature2(self):
        print("Feature2 working")

class B:

    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature 1-B working")
    def feature4(self):
        print("Feature4 working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C init")

    def feature5(self):
        print("Feature5 working")
    def feature6(self):
        print("Feature6 working")

c1 = C()
c1.feature1()



print()

















































