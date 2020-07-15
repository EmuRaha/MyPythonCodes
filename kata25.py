

def perimeter(n):
    sum1=1
    num=1
    lst=[1,1]
    for i in range(n-1):
        sum2=sum1+num
        num=sum1
        sum1=sum2
        lst.append(sum2)

    return 4*sum(lst)

print(perimeter(5))















