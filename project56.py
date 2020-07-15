# Multi-Threadind

from time import  sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)




c1 = Hello()
c2 =Hi()

c1.start()
sleep(0.2)
c2.start()
c1.join()
c2.join()
print("Bye")








































