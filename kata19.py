

def digital_root(n):
    while len(str(n)) > 1:
        a = sum([int(i) for i in str(n)])
        n = a
    return n


print(digital_root(7))



# a = sum([int(i) for i in str(n)])























