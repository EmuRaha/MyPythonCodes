# File Handling

f = open("MyText","r")
#print(f.read())
print(f.readlines())
print(f.readlines())
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())



f1 = open("MyFile","w")

for i in f:
    f1.write(i)


f1.write("This is my file. I want to write something.")
f1 = open("MyFile","r")
#print(f1.read())

print(f.readlines(1))
print(f.readlines())
#print(f.readline(3))
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())


p1 = open('Emu.jpg','rb')

p2 = open('MyPic.txt','wb')

for line in p1:
    p2.write(line)



























