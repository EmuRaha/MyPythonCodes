
class computer:
    def __init__(self):
        self.name = "Emu"
        self.age = 21
    def update(self):
        self.age = 51
    def compare(self,other):
        return self.age == other.age
c1 = computer()
c2 = computer()
print(id(c1))
print(id(c2))

print(c1.age)
c1.update()
print(c1.age)
c2.age = 52
print(c2.name,c2.age)

if c1.age == c2.age:
    print("They are same")
else:
    print("They are different")

print(c1.compare(c2))

c3 = computer()

print(c3.compare(c1))

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")






















