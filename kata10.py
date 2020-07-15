


def is_triangle(a, b, c):
   x=sorted([a,b,c])
   if x[2]<x[1]+x[0]:
       return True
   else:
       return False








def is_triangle(a, b, c):
   x=sorted([a,b,c])
   return x[2]<x[1]+x[0]

print(is_triangle(7,3,5))






















