# Get the Middle Character
# You are going to be given a word.
# Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    n=len(s)
    if n%2==0:
        l=n/2
        print(s[int(l-1)]+s[int(l)])

    else:
        l=n/2
        print(s[int(l-0.5)] )

get_middle("test")
get_middle("mango")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")




print()
print()

def get_middle(s):
    n=len(s)
    if n%2==0:
        l=int(n/2)
        print(s[l-1]+s[l])

    else:
        l=int((n-1)/2)
        print(s[l])
get_middle("test")
get_middle("mango")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")

print()
print()

def get_middle(s):
    n=len(s)
    if n%2==0:
        l=int(n/2)
        print(s[l-1]+s[l])

    else:
        l=int(n/2)
        print(s[l])
get_middle("test")
get_middle("mango")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")


















