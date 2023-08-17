#lamba arguments: expression
add10 = lambda x: x+10
# print(add10(5))

mult = lambda x,y: x*y
# print(mult(2,3))

points2D = [(1,2), (15,1), (5, -1), (10,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

# print(points2D)
# print(points2D_sorted)

a = [1, 2, 3, 4, 5]
#map(func, seq)
b = map(lambda x: x*2, a)
print(list(b))

#filter(func, seq)
c = filter(lambda x: x%2==0, a)
print(list(c))

#reduce(func, seq
from functools import reduce
d = reduce(lambda x,y: x*y, a)
print(d)
