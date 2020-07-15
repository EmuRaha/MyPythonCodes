

def pig_it(text):
    text = text.split()
    lst=[]
    for i in text:
        if i.isalpha()==False:
            lst.append(i)
        else:
            b=i[1:]+i[0]+"ay"
            lst.append(b)
    return " ".join(lst)

    


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))


















