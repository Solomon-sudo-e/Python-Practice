# Tuples are ordered, immutable, allows duplicate elements.
#Parenthesis are OPTIONAL
my_tuple = "Max", 28, "Boston"
print(my_tuple)
#If only adding one element in a tuple, add a comma at the end to allow it to be recognized as a tuple.

tuple_with_one_element = ("Max",)
tuple_with_tuple_address = tuple(["john", "mark", "brian"])

name = tuple_with_tuple_address[0]
#print(name)

for i in tuple_with_tuple_address:
    print(i)

if "john" in tuple_with_tuple_address:
    print("welcome home john")
else:
    print("no john here")

length_of_tuple = len(tuple_with_tuple_address)
print(length_of_tuple)

print(tuple_with_tuple_address.count('brian')) #Gives count of how many times it is used.
print(tuple_with_tuple_address.index("brian")) #Gives place that it is

#You can convert tuples and list to eachother.
newlist = list(tuple_with_tuple_address)
print(newlist)

tuplehome = tuple(newlist)
print(tuplehome)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[1:5:3] #Starts after one and steps over three onto 5.
print(b)

name_age_city = "Salmon", 21, "Siloam Springs"
name, age, city = name_age_city
print(name)
print(age)
print(city)
#Must match place of each variables.

tuple_with_numbers = 1, 2, 3, 4, 5, 6, 7, 8
i1, *i2, i3 = tuple_with_numbers
print(i1)
print(i2) #The star tells it to grab every element inbetween
print(i3)

#Tuple can be more efficient sometimes. (TUPLE IS LESS BYTES

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) #Tuples take less time to create too.
