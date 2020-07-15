
def pascal(n):
    pas = []
    previous = []
    for i in range(0,n):
        current = [1 for i in range(i+1)]
        if i>1:
            for j in range(1,i):
                current[j]= sum(previous[j-1:j+1])
        pas.append(current)
        previous = current
    return pas
print(pascal(7))

def pascal(n):
    pas = []
    previous = []
    for i in range(0,n):
        current = [1 for i in range(i+1)]
        if i>1:
            for j in range(1,i):
                current[j]= sum(previous[j-1:j+1])
        a = " ".join(str(i) for i in current )
        b = "".join(" " for i in range(n-i))
        c= "".join([b,a])

        pas.append(c)
        previous = current
    return "\n".join(pas)
print(pascal(5))





































