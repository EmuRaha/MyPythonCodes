#Take 2 strings s1 and s2 including only letters from ato z.
#Return a new sorted string, the longest possible, containing distinct letters,

#each taken only once - coming from s1 or s2.

def longest(s1,s2):
    x=set()
    for i in s1+s2:  #x=set(s1+s2)
        x.add(i)
    y=sorted(x)
    for j in y:
        print(j,end="")

    print()

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

longest(a,b)

a = "abcdefghijklmnopqrstuvwxyz"
longest(a,a)


def longest1(s1,s2):
    return "".join(sorted(set(s1+s1)))

print(longest1(a,b))


















