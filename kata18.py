



def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True



print(is_prime(17))
print(is_prime(98274320984709))

def is_prime1(num):
    import math
    if num<2:
        return False
    max_divisor = math.floor(math.sqrt(num))
    for i in range(2,max_divisor+1):
        if num%i==0:
            return False
    return True



print(is_prime1(17))
print(is_prime1(98274320984709))



def is_prime2(num):
    import math
    if num<2:
        return False
    if num==2:
        return True
    if num>2 and num%2==0:
        return False
    max_divisor = math.floor(math.sqrt(num))
    for i in range(3,max_divisor+1,2):
        if num%i==0:
            return False
    return True



print(is_prime2(17))
print(is_prime2(98274320984709))


















