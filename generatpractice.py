
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

# print(sorted(g))

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

# cd = countdown(4)
# value = next(cd)

#Generators are great for saving menory when working with large data

def firstn(n):
    nums=[]
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


# import sys
# print(sys.getsizeof(firstn(100000)))
# print(sys.getsizeof(firstn_generator(100000)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(100)
# for i in fib:
    # print(i)

import sys
mygenerator = (i for i in range(100000) if i % 2 == 0)
print(sys.getsizeof((mygenerator)))
mylist = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(mylist))










