#Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities.
#"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.


def comp(a1,a2):
    if a1==None or a2==None:
        return False

    if sorted(a2)==sorted(i*i for i in a1):
        return True

    return False






a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1,a2))

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False