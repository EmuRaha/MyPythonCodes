def josephus(n,k):
    items=[l for l in range(1,n+1)]
    if items == []:
        return 0
    if len(items)==1:
        return items[0]
    i = k - 1
    new = []
    if k>len(items):
        i=i%len(items)
    j=items[i]

    while j in items:
        new.append(j)
        items.pop(i)

        if len(items) > 1:
            i = i + k - 1
            if i > len(items) - 1:
                i = i%len(items)
            j = items[i]

        else:
                break

    return items[0]

print(josephus(7,3))


