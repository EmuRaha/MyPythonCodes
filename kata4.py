#Shortest Word
#Simple, given a string of words, return the length of the shortest word(s).
#String will never be empty and you do not need to account for different data types.

def short(s):
    a= s.split()
    b=[]
    for i in a:
        b.append(len(i))
    return min(b)
s="bitcoin take over the world maybe who knows perhaps"
print(short(s))
s="turns out random test cases are easier than writing out basic ones"
print(short(s))
s="lets talk about javascript the best language"
print(short(s))
s="i want to travel the world writing code one day"
print(short(s))
s="Lets all go on holiday somewhere very cold"
print(short(s))













print()
print()
print()
def short1(s):
    return min(len(x) for x in s.split())


s="bitcoin take over the world maybe who knows perhaps"
print(short1(s))
s="turns out random test cases are easier than writing out basic ones"
print(short1(s))
s="lets talk about javascript the best language"
print(short1(s))
s="i want to travel the world writing code one day"
print(short1(s))
s="Lets all go on holiday somewhere very cold"
print(short1(s))
















