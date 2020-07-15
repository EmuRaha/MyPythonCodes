

class student:

    school = "MGGHS"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):           #instance method(2 types)
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):        #1.accessors
        return self.m1

    def set_m1(self,value):  #2.mutators
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        return "This is my class. Do whatever you want."




s1 = student(12,34,56)
s2 = student(34,56,78)

print(s1.avg())
print(s2.avg())


print(s1.get_m1())

s1.set_m1(58)

print(s1.get_m1())

print(s1.avg())
print(s2.avg())


print(student.getSchool())

print(student.info())



















