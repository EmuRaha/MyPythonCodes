
class computer:

    def config(self):
        print("i5, 16GB, 1TB")
a = 5
comp1 = computer()
comp2= computer()
print(type(a))
print(type(comp1))
computer.config(comp1)
computer.config(comp2)
#or
comp1.config()
comp2.config()

class computer:

    def __init__(self):
        print('in init')

    def config(self):
        print("i5, 16GB, 1TB")


comp1 = computer()
comp2= computer()

comp1.config()
comp2.config()


class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config of is:",self.cpu, self.ram)


comp1 = computer('i5',16)
comp2 = computer('ryzen 3',8)

comp1.config()
comp2.config()

class computer:

    def config(self,cpu,ram):
        self.c = cpu
        self.r = ram
        print("config of is:",self.c, self.r)


comp1 = computer('i5',16)
comp2 = computer('ryzen 3',8)

comp1.config()
comp2.config()

class computer:

    def config(self,cpu,ram):
        self.c = cpu
        self.r = ram
        print("config of is:",self.c, self.r)


comp1 = computer()
comp2 = computer()

comp1.config('i5',16)
comp2.config('ryzen',8)





















