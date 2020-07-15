

def sum_dig_pow(a, b):
    lst=[]
    for i in range(a,b+1):
        if sum(int(str(i)[n])**(n+1) for n in range(len(str(i))))==i:
            lst.append(i)
    return lst



print(sum_dig_pow(89,135))

print(sum_dig_pow(90, 100))























