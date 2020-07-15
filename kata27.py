

def move_zeros(array):
    l = array.count('0') + array.count('0.0')
    lst=[]
    for i in array:
        if type(i)==str:
            lst.append(i)
        lst.append(str(i))
    n = lst.count('0')+ lst.count('0.0')-l
    n=n-l
    lst1 = []
    for i in array:
        if type(i)==str:
            lst1.append(i)
        if type(i)!=str and str(i) != '0' and str(i)!='0.0':
            lst1.append(i)
    for j in range(n):
        lst1.append(0)
    return lst1


print(move_zeros([False,1,0,1,2,0,1,3,"a"]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,'0',"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print(move_zeros([]))


















