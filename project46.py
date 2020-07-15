

class student:


    def __init__(self,name,rollno):
        self.name = name
        self.roll = rollno
        self.lap = self.Laptop()



    def show(self):
        print(self.name,self.roll)


    class Laptop:

        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8


        def show(self):
            print(self.brand,self.cpu,self.ram)



s1 = student("Emu",38)
s2 = student("TYB",1)

s1.show()
s1.lap.show()

s2.show()
s2.lap.show()

































































