

dic={2:2354,1:456,3:32,5:78,4:9}



b=dic.items()

a= sorted(b)

print(a)

for i,j in a:
    print(j,end=" ")


print()


#your task is to sort a given string. each word in the string will contain a single number.
# this number is the position the word should have in the result.
# note: numbers can be from 1 to 9. so 1 will be the first word (not 0).
# if the input string is empty, return an empty string.
# the words in the input string will only contain valid consecutive numbers.

def order(sentence):
    dic1={}
    sentence=sentence.split()
    for i in sentence:

        for j in i:
            if j in "123456789":
                dic1[j]=i

    b = dic1.items()

    a = sorted(b)

    return " ".join(l for k,l in a)



print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))






print()
print()
print()
print()














