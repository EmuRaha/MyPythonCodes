p1 = open('Emupic.jpg','rb')
p2 = open('Emupic1.jpg','wb')

for line in p1:
    p2.write(line)
