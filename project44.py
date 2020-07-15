
#different types of variables

class car:

    wheels = 5


    def __init__(self):
        self.mileage = 10     #instance variable
        self.company = "BMW"  #instance variable




c1 = car()
c2 = car()

print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)

c2.mileage = 8
car.wheels = 4

print(c1.company,c1.mileage,c1.wheels)
print(c2.company,c2.mileage,c2.wheels)


































































