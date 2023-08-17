import random

a = random.random()
# print(a)

b = random.uniform(10, 100)
# print(b)

c = random.randint(10, 100)
# print(c)

d = random.randrange(10, 100) # this will never pick the upper bound variable

e = random.normalvariate(0, 1) #Allows for use for mu and sigma means. See mu/sigma statistics graph
# print(e)


# random.seed(1)
# print(random.random())
# print(random.randint(1,10))
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(1)
# print(random.random())
# print(random.randint(1,10))
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

mylist = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
f = random.sample(mylist, 3)  #Will pick unique, not multiple.
# print(f)

g = random.choices(mylist, k=3) #Allows duplicated
# print(g)

h = random.shuffle(mylist)
# print(h)

#Randoms are not recommended for security.
#Use this, only problem is that they take more time.
import secrets

i = secrets.randbelow(10)
# print(i)

j = secrets.randbits(4)
# print(j)

k = secrets.choice(mylist)
# print(k)

import numpy as np

l = np.random.rand(8,8)
# print(l)

m = np.random.randint(0,10,(8,8))
# print(m)

n = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(n)
np.random.shuffle(n)
print(n)
np.random.seed(1) #To create a seed in numpy, used this.









