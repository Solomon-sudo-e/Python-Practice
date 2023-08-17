#List are orders, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
#print(mylist)

item1 = mylist[-2]
#print(item1)

#for fruit in mylist:
#    print(fruit)

if "banana" in mylist:
    print("There is a banana!")
else:
    print("no banana ):")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(0, "blueberry")
print(mylist)

item = mylist.pop()
print(item)

remove_item = mylist.remove("blueberry")
print(mylist)

mylist.reverse()
print(mylist)

new_list = sorted(mylist) #ALPHABETICAL ORDER
print(new_list)

number_list = [0] * 5
print(number_list)

concat_list = new_list + number_list
print(concat_list)

slice_list = [1,2,3,4,5]

a = slice_list[1:4] #removed first and last numbers using slice.
print(a)

b = slice_list[1:] #Continues after first index, same for the stop.
print(b)

c = slice_list[::2] #Takes every second item.
print(c)

d = slice_list[::-1] #Just reverses list
print(d)

list_cpy = mylist

# list_cpy.append("lemon")
# print(list_cpy)               THIS COPIES TO BOTH LIST
# print(mylist)

#To prevent
# list_cpy = list(mylist)
# list_cpy = mylist[:]
print(list_cpy)

#List comprehension
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Syntax [expression then (for) (in) loop]
squared_number_list = [i*i for i in number]
print(squared_number_list)
