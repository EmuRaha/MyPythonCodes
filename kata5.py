#Disemvowel Trolls
#rolls are attacking your comment section!

#A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

#Your task is to write a function that takes a string and return a new string with all vowels removed.

#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

#Note: for this kata y isn't considered a vowel.

def disemvowel(string):      #error when attempt
    a=string.split()
    c=[]
    for i in a:
        b=[]
        for j in i:
            if j in "aeiouAEIOU":
                continue
            b.append(j)
        d="".join(j for j in b)
        c.append(d)
    return " ".join(k for k in c)
v=disemvowel("This website is for losers LOL")

print(v)


def disemvowel1(string):        #submitted
    for i in "aeiouAEIOU":
        string = string.replace(i,"")
    return string
v=disemvowel1("This website is for losers LOL")

print(v)






































