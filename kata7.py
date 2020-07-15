# Beginner Series #3 Sum of Numbers
# Given two integers a and b, which can be positive or negative,
# find the sum of all the numbers between including them too and return it.
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!


def get_sum(a,b):
    if a<b:
        return sum(range(a,b+1))
    else:
        return sum(range(b,a+1))
print(get_sum(0,10))
print(get_sum(0,-1))
print(get_sum(3,-3))
print(get_sum(1,1))

def get_sum(a,b):
    return sum(range(min(a,b),max(a,b)+1))
print(get_sum(0,10))
print(get_sum(0,-1))
print(get_sum(3,-3))
print(get_sum(1,1))






















