# # Sets are unordered, mutable, no duplicates allowed.
#
# myset = set("Hello")
# print(myset) #Good for figuring out how many unique keys we have.
#
# #Empty sets must be recognized as a set or it will be shown as a dictionary.
#
# print(type(myset))
#
# myset.add(1)
# myset.add(2)
# myset.add(3)
# print(myset)
#
# try:
#     myset.remove(4)
# except:
#     print("no value of 4")
#
# #So we use VVVV in order to remove IF we have that element and continue if not.
# # myset.discard(4)
# # print(myset.pop()) #Returns a random value of the set and removes it from the set.
# # # myset.clear will clear the set
# # print(myset)
#
# # for i in myset:
# #     print(i)
# #
# # if 1 in myset:
# #     print("1 is in the set")
# # else:
# #     print("There is no 1 in the set.")
# #
#
#
#
#

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)
#Union combines two sets without duplication

i = odds.intersection(primes)
print(i) #Gives all values that are the same.

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
#
# difference = setA.difference(setB)         #Self explanatory mostly, gives the values that arent the same.
# difference_of_setB = setB.difference(setA) #from the second set.
# print(difference)
# print(difference_of_setB)
#
# symmetric_difference = setA.symmetric_difference(setB) #Gives all values that are unique to
#                                                        # both sets but none that are the same/
# print(symmetric_difference)

# setA.intersection_update(setB)
# print(setA) #Updated only to have similar values.

# setA.update(setB)
# print(setA) #Updates the set by adding all NEW elements.

# setA.difference_update(setB) #Removes all elements that are inside of setB from setA
# print(setA)

# setA.symmetric_difference_update(setB) #Takes all elements that are unique to both sets.
# print(setA)

# print(setA.issubset(setB)) #Checks if is setB only has values that are in setA.

# print(setB.issuperset(setA)) #Is not super set because setB does not contain all of the elements of setA.

# print(setA.isdisjoint(setB)) #Has the same elements inside of eachother

#Copying has the same things as dictionaries and list.

#Frozen sets.

a = frozenset({1, 2, 3, 4, 5})
#This means the set is now immutable.
print(a)


