#itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product
x = [1, 2]
y = [3]
prod = product(x,y, repeat=2) #Will give the cartesion product of the sets.
# print(list(prod))

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a) #Permutations give all variations in which a set can be ordered.
# print(list(perm))

from itertools import combinations
comb = [1, 2, 3]
combination = combinations(comb, 2)
# print(list(combination))

from itertools import combinations_with_replacement
replace = [1, 2, 3]
combinations_with_replacement = combinations_with_replacement(replace,2)
# print(list(combinations_with_replacement))
#Allows repeated elements.

from itertools import accumulate
import operator
accumulated = [1, 2, 3, 4]
acc = accumulate(accumulated) #Added things up.
mul = accumulate(accumulated, func=operator.mul)
# print(accumulated)
# print(list(acc))
# print(list(mul))

from itertools import groupby
# def smaller_than_3(x):
#     return x < 3
# groupie = [1, 2, 3, 4]
# group_obj = groupby(groupie, key=lambda x: x<3) #using lambda instead of the function.
# for key, value in group_obj:
#     print(key, list(value))
#Compared everything inside the list then groups them in a dictionary (techincally).

from itertools import count, cycle, repeat
for i in count(10):
    print(i)
    if i == 15:
        break
list = [1, 2, 3]
for i in cycle(list):
    print(i)


for i in repeat(1, 10):
    print(i)



