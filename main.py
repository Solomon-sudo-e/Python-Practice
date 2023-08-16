from math import *
import useful_tools
import docx
from dog import Dog
from question import Question

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
#
# character_name = "Solomon"
#
# print(character_name)
#
# age = 50.55
# is_hot_outside = True, False
#
# print(is_hot_outside)
# print("PrintQuotation\"\"BetweenString")
# phrase = "My name Salmon"
#
# # functions
#
# print(phrase.lower())
# print(phrase.isupper())  # Checks if string is all upper case and returns T or F value. Same is islower()
# print(phrase.upper())
# print(len(phrase))  # Checks length of string.
# print(phrase[13])  # Gives first letter or whatever letter is indexed.
# print(phrase.index("n"))  # Gives index of where letter is the first time.
# print(phrase.replace("Salmon", "Dog"))  # Replaces parts of string given proper words or letters.
# print(
#     str(age))  # converts the age integer into a string. You have to make numbers a string to print with other strings.
#
# #Common functions
#
# number = 100
#
# print(abs(number)) #Gives absolute value of a number
# print(pow(number, 2))  #Raises a number to the power of n, 100^2 in our case.
# print(max(number, 20))  #Gives the bigger number.
# print(min(number, 20))
# print(round(100.7)) #Self explanatory
# print(floor(3.7)) #Gives round down,
# print(ceil(3.7)) #Gives round up
# print(sqrt(100))
#
# my_name = input("Enter your name loser:")
# age = input("Enter your age:")
# print("Hello " + my_name + ". You are " + age )
#

# num1 = input("Enter your first number:")
# num2 = input("Enter your second number:")
# result = float(num1) + float(num2)
# print(result)


# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

#LIST
# developers = ["Matt", "Michael", "Alex", "Salmon", "Stephanie"]
# print(developers[-1]) #End of list
# print(developers[1:4]) #Gives a range of index and last number is the one it will stop before.
# developers[1] = "Stein"
# print(developers)
# dogs : list[str] = ["Dog", "Dog2"]
# print(dogs)
#
# lucky_numbers = [4,8,15,16,23,42]
# developers.append("Michael")
# developers.remove("Matt")
# developers.pop() #Removes last element in list. (Michael)
# print(developers)
# print(developers.index("Salmon")) #Prints where salmon is in the list.
# print(developers.count("salmon"))
# print(developers.sort()) #Sorts in alphabetical order in this case.
# developers.clear()
# developers.extend(lucky_numbers)
# print(developers)
# print(lucky_numbers.reverse())
# lucky_numbers_copy = lucky_numbers.copy()

#Tuples
#Tuples are immutable
#coordinates = [(4,5), (6,8), (7,9)]

#Functions that I create
# def say_hi(name, age):
#     print("Hi " + name + ", you're " + str(age) + " old")
#
# say_hi("Solomon", 21)
#
# def cube_numbers(num):
#     return num*num*num
#
# print(cube_numbers(10))

#If/else Statements
# is_male = True
# is_tall = True
# if is_male and is_tall:  #Variable is set to true to its accepted
#    name = input("Please enter your name: ")
#    print(name + " is a tall male")
# elif is_male and not(is_tall):
#     name = input("Please enter your name: ")
#     print(name + " is male and not tall")
# elif not(is_male) and is_tall:
#     name = input("Please enter your name: ")
#     print(name + " is tall and not male")
# else:
#     print("This person is not male and is short")

#More advanced if/else statements

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(213,52345,43214321))

#More advanced calculator lol

def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    num1 = float(input("Please enter the first number: "))
    op = input("Please select what operation you would like to use: ")
    num2 = float(input("Please enter the second number: "))
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "%":
        return num1 % num2
    else:
        return print("Please select a valid operation")

#print(calculator())

#Dictionaries

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
#
# print(monthConversions["Jan"])
# print(monthConversions.get("dog", "Not a valid key"))
# print(monthConversions)

#While loop
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Loop done lol")


#Guessing game

# secret_word = "dog"
# guess = input("Guess the secret word! Here:")
# i = 1
# while secret_word != guess and i < 3:
#     guess = input("Try again! Guess here:")
#     if i == 3:
#         print("Three strikes, youre out!")
#     if secret_word == guess:
#         break
#     i += 1
# if not(i == 3):
#     print("You won!")



#For loops

    #Enhanced for loop
# for index in range(200) :
#     print(index)


#Exponent Function

# print(2**3)
#
# # "**" raises numbers to that power.
# #Now ill make my own function to do this.
#
# def exponent(num, power):
#     result = 1
#     for count in range(power) :
#         result *= num
#     return result
#
#
# print(exponent(10, 6))



#2D List
#
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# #print(number_grid[2][1])
#
# #Nested for loop for this list
#
# for row in number_grid:
#     for col in row:
#         print(col)


#Building a basic translator

# def translator(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "L"
#             else:
#                 translation = translation + "l"
#         else:
#             translation = translation + letter
#     return translation
#
#
# print(translator("dOg"))




#Try / Except (Java try/catch)
# try:
#     number = int(input("Enter a integer"))
#     print(number)
# except ValueError as err:
#     print(err)


#Reading external files
#There is different modes for files. "r" (Read) "w" (Write) "a" (Append) "r+" (Read & Write)
# WRITE WILL OVERRIDE ENTIRE FILE OR CREATE NEW FILE
# file = open("people_list", "r")
# for people in file.readlines():
#     print(people)
# file.close()

# file = open("people_list", "a")
# file.write("\nAlex - Developer")

#Safe practice is to make a new file for it and copy it. (I think) (I just made it up on the spot)
# file_new = open("people_listNEW", "r+")
# file_new.write(file.read())


#Modules / Pips
#Modules are classes.
#docs.python.org has many modules.

# print(useful_tools.roll_dice(10))
#Imported docx to be used. Then I made a dog which is my dog

dog1 = Dog(
    "Marvin", "chocolate_labradoodle",
    True, "brown",
    60, "male",
    "The Goodest")
# print(dog1.was_good_doggo())
# print(dog1.weight)
print(dog1.is_mammal())

question_prompts = [
    "What is salmons favorite color?\n(a)red\n(b)blue\n(c)black\n\n",
    "What is salmons main coding language?\n(a)java\n(b)c#\n(c)python\n\n",
    "What is Salmons favorite drink?\n(a)water\n(b)protein shakes\n(c)energy drinks\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " questions right!")

# run_test(questions)

