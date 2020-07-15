

def div(a,b):
    return a/b



def smart(f):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return f(a,b)
    return inner

div=smart(div)

print(div(2,4))




def sum(a):

    def sum1(b):
        return a+b
    return sum1


d= sum(3)
print(d(2))



























