#Strings, are ordered, immutable, text representation

my_string = 'Hello World'
triple_quotes = """Hello \
my fellow developer"""
#print(my_string)
#print(triple_quotes)

string = "Hi salmon"
ca = string[0] #Char
#print(ca)

substring = string[-1::-1]

#print(substring)

# for i in string:
#     print(i)

# if "hi" in string.lower():
    # print("Hi how are you!")
# else:
    # print("go away")

whitespace = "          space       "
cleaned = whitespace.strip()
# print(cleaned)

# print(string.lower().startswith("hi"))
# print(string.upper().find("S")) #Finds index

# print(my_string.replace("World", "Galaxy"))

string_list = my_string.split() #Default argument is to split at a space.
print(string_list)

new_string_from_list = " ".join(string_list)
print(new_string_from_list)

# String formats
# %, .format(), f-Strings
var = "Tom"
int = 3
floating_point = 3.1459
# tom_string = "the variable is %s" % var
# number_string = "the variable is %d" % int
# floating_point_string = "the variable is %f" % floating_point
# print(number_string)
# print(floating_point_string)
# print(tom_string)

#Placeholder strings
# tom_string = "the variable is {}".format(var)
# number_string = "the variable is {:.2f} and {}" .format(floating_point, int)
# print(number_string)
# print(floating_point_string)
# print(tom_string)

tom_string = f"the variable is {var}"
number_string = f"the variable is {int}"
floating_point_string = f"the variable is {floating_point}"
print(number_string)
print(floating_point_string)
print(tom_string)
