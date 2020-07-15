
import sys

print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i=i+1
    print(i,'Hello')
    greet()




sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i=i+1
    print(i,'Hello')
    greet()
greet()




















