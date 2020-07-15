def solution(args):
    lst=[]
    i=args[0]
    while i in args:
        n= args.index(i)
        if i+1 not in args:
            lst.append(str(i))
            if n<(len(args)-1):
                i = args[n + 1]
            else:
                break
        else:
            lst2 = []
            lst2.append(i)

            while i + 1 in args:
                lst2.append(i + 1)
                i = i + 1
            if len(lst2) == 2:
                j = f"{str(lst2[0])},{str(lst2[-1])}"
            else:
                j = f"{str(lst2[0])}-{str(lst2[-1])}"
            lst.append(j)
            if args.index(lst2[-1]) < (len(args) - 1):
                i = args[args.index(lst2[-1]) + 1]
            else:
                break
    return ",".join(lst)









print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))

































