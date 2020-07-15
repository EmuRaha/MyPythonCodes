

def josephus(items,k):
    if items == []:
        return []
    i = k - 1
    new = []
    if k>len(items):
        i=i%len(items)
    j=items[i]

    while j in items:
        new.append(j)
        items.pop(i)

        if items != []:
            i = i + k - 1
            if i > len(items) - 1:
                i = i%len(items)
            j = items[i]

        else:
                break

    return new

print(josephus([1,2,3,4,5,6,7],3))
print(josephus([1,2,3,4,5,6,7,8,9,10],1))
print(josephus([1,2,3,4,5,6,7,8,9,10],2))
print(josephus(["C","o","d","e","W","a","r","s"],4))
#[3, 6, 2, 7, 5, 1, 4])
print(josephus([],3))


print(josephus([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],40))

print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 11))

print(josephus([True, False, True, False, True, False, True, False, True],9))





