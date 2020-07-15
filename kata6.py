# Descending Order
# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.



def descending_order(num):
    return int("".join(str(j) for j in sorted(list(int(i) for i in str(num)),reverse=True)))           #int objectv is not iterable, converted into str



print(descending_order(2334))

def descending_order1(num):
    return int("".join(sorted(str(num), reverse=True)))                     #int objectv is not iterable, converted into str


print(descending_order1(2334))



















