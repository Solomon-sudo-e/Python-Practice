# # Dictionary: Key-value pairs, unordered, mutable, (Like java hash)
#
# mydict = {"name": "Salmon",
#           "age": 21,
#           "city": "Siloam Springs"}
# print(mydict)
#
# mydict2 = dict(name="Skylar", age=21, city="Bentonville")
# print(mydict2)
#
# value = mydict["name"]
# print(value)
#
# mydict["email"] = "solo.hufford@gmail.com"
# print(mydict)
#
# del mydict["name"]
# print(mydict)
#
# mydict.pop("age")
# print(mydict)
#
# mydict.popitem() #Removes last inserted item.
# print(mydict)
#
# if "name" in mydict2:
#     print(mydict2["name"])
#
# try:
#     print(mydict["email"])
# except:
#     print("error no email")
#
# #looping through dictionaries
#
# for key, value in mydict2.items():
#    print(key, value)
#
#
# #Copying dict
# #Will be modify on both dictionaries if not copied correctly.
# mydict2_cpy = dict(mydict2)
# print(mydict2)
# mydict2_cpy["email"] = "skylar@skylar@gmail.com"
# print(mydict2_cpy)
#
#

my_dict = dict(name = "Mary", age = 27, city="boston")
my_dict2 = {"name": "John", "age": "22", "city": "new york"}

my_dict.update(my_dict2) #Overwrites the old dict with a new dict.
print(my_dict)


#Tuples can be inside of dictionaries as keys or values.
