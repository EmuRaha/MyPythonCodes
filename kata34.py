
# Not efficient

def dbl_linear(n):

    lst =[1]

    for i in range(n):
        x = lst[i]
        y = 2 * x + 1
        z = 3 * x + 1
        lst.append(y)
        lst.append(z)
        lst = sorted(set(lst))

    return lst[n]

print(dbl_linear(10))
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(50))
print(dbl_linear(100))
print(dbl_linear(5000))












































