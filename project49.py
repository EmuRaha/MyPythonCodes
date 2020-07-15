# Polymorphism
# Duck-Typing

class MyEditor:


    def execute(self):
        print("compiling")
        print("running")


class PyCharm:

    def execute(self):
        print("compiling")
        print("running")


class Laptop:

    def code(self,ide):
        ide.execute()

IDE1 = PyCharm()
IDE2 = MyEditor()

lap1 = Laptop()

lap1.code(IDE1)
print()
lap1.code(IDE2)

print()

class Duck:
    def fly(self):
        print("Duck flying")

class Sparrow:
    def fly(self):
        print("Sparrow flying")

class Whale:
    def swim(self):
        print("Whale swimming")

for animal in Duck(), Sparrow(), Whale():
    try:
        animal.fly()
        print("It's a bird")

    except:
        animal.swim()
        print("it's not a bird")


























