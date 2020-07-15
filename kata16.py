

def iq_test(numbers):
    numbers = [int(a) for a in numbers.split()]
    even = [i for i in numbers if i%2==0]
    odd  = [i for i in numbers if i%2!=0]
    if len(even)==1:
        a = even[0]
        return numbers.index(a)+1
    else:
        a = odd[0]
        return numbers.index(a)+1



print(iq_test("2 4 7 8 10"))

