
List = [456,1,2,34,65,7,9,8,6,35,-5,345,0]
sorted_List = []


for i in range(len(List)):
    min = List[0]
    for i in List:
        if i<min:
            min = i
    List.remove(min)
    sorted_List.append(min)





print(sorted_List)



































