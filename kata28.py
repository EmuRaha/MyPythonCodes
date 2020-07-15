

def dirReduc(arr):  #takes a lot of time
    i=arr[0]

    while i in arr:
        n = len(arr)

        if i=="NORTH" and arr[arr.index(i)+1]=="SOUTH" or i=="SOUTH" and arr[arr.index(i)+1]=="NORTH":
            arr.remove("NORTH")
            arr.remove("SOUTH")
        elif i=="EAST" and arr[arr.index(i)+1]=="WEST" or i=="WEST" and arr[arr.index(i)+1]=="EAST":
            arr.remove("EAST")
            arr.remove("WEST")
        if len(arr)==n:
            i=arr[arr.index(i)+1]
        else:
            i=arr[0]
        if arr.index(i) == len(arr) - 1:
            break
    return arr

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))



def dirReduc(arr): #time efficient
    n=0
    while n<len(arr)-1:
        l=len(arr)
        if (arr[n]=="NORTH" and arr[n+1]=="SOUTH") or  (arr[n]=="SOUTH" and arr[n+1]=="NORTH") or (arr[n]=="EAST" and arr[n+1]=="WEST") or  (arr[n]=="WEST" and arr[n+1]=="EAST"):
            del arr[n:n+2]
        if len(arr)==l:
            n=n+1
        else:
            n=0
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["WEST", "SOUTH", "EAST","NORTH"]))



















