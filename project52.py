


class computer:

    def process(self):
        pass

com = computer()
com.process()


from abc import ABC,abstractmethod

class computer(ABC):

    @abstractmethod
    def process(self):
        pass

#com = computer()    #(error)
#com.process()

class computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(computer):

    pass

#com = Laptop()      #(error)
#com.process()

class computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(computer):

    def process(self):
        print("It's running")

class whiteboard:

    def write(self):
        print("Its writting")

class Programmer:

    def work(self,comp):
        print("solving bugs")
        comp.process()

com1 = Laptop()
prog = Programmer()

wb = whiteboard()
prog.work(com1)
#prog.work(wb)       #error
























