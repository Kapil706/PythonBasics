print("Hello World")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "John"

character_age = "35"
is_Male = True

print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
print("He really liked the name " + character_name)
print("but didn't like being called " + character_age)

phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("G"))
print(phrase.replace("Giraffe", "Elephant"))
print("The Meetup \nVlogger")
print("Giraffe \" Academy")

print(2)
print(-2)
print(3 + 4.5)
my_num = 5
print(my_num)

print(str(my_num) + " my favourite number")

num = -5
print(abs(num))
print(pow(4, 6))
print(max(4, 6))
print(min(4, 6))
print(round(3.56784))

import math

print(math.floor(3.7))
print(math.ceil(3.7))
print(math.sqrt(36))

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
"result = num1+num2"
"result_h = int(num1)+int(num2)"
result_g = float(num1) + float(num2)

"print(result)"
"print(result_h)"
print(result_g)

print("Madlibs game ")

color = input("Enter a color: ")
plural_noun = input("Enter a Plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

"Lists "

"structure we use to store bunch of related values"

friends = ["Kevin", "Karen", "Jim"]

"Inside lists we can put strings , intergers, boolean"

print(friends)

"each element has index in list"
print(friends[0])
print(friends[2])
"negative index gives access of elements from the last"
print(friends[-1])

print(friends[1:])
"It gives elements at position specified and after that"

print(friends[1:3])

"modify elements in list"

friends[1] = "Mike"

"List functions"

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends1)

"extend function adds one list wit other"

friends1.extend(lucky_numbers)

"append function adds items to the end of the list"

friends1.append("Creed")

"insert function to insert elements at specified position "
friends1.insert(1, "Kelly")
"index position and element"

"remove elements "

friends1.remove("Jim")

friends1.clear()
"get rid of every element in the list"

friends.pop()
"pop out the last element in the list"

# print(friends1.index(2))

"Count no of similiar elements in the list"

print(friends1.count("Jim"))
"how many time jim shows up oin the list"

print(friends1.sort())
"sort elements alphabetically"

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends1.copy()

"Tuples"
"It is Immutable "
"it is a container where we can store mutiple data"

coordinates = (4, 5)
print(coordinates[0])
"pass index"

"difference between tuple and list is inside tuple data can not be modified"

" functions"


def say_hi(name, age):
    print("Hello User")
    print("Hello " + name + ", you are " + str(age))
    "always name function in lowercase""Return Statement"
    print("Top")
    say_hi("Mike", 35)
    say_hi("Steve", 70)
    print("Bottom")


def cube(num):
    "after return statement no code line will run if breaks the function and pass control next line to function"
    return num * num * num


result_c = cube(4)
print(result_c)

"If statements"

is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a Male or tall or both ")
elif is_male and not (is_tall):
    print("You are a short Male ")

elif not (is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a Male and not tall")

"Comparisons"


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


(max_num(3, 4, 5))

num5 = float(input("Enter first number :"))
op = input("Enter operator: ")
num4 = float(input("Enter the second number :"))

if op == "+":
    print(num5 + num4)
elif op == "-":
    print(num5 - num4)
elif op == "/":
    print(num5 / num4)
elif op == "*":
    print(num5 * num4)
else:

    print("Invalid operator")

"Dictionaries are used to store key-value pair"

monthConversions = {

    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    4: "August",

}

print(monthConversions["Jan"])

print(monthConversions.get("dec", "Not a valid key"))
"using this we get a default value if the mapping is not done correctly"

"While Loop in python is structure that will loop through specific line of code"

i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with while loop")

"building a guessesing game"

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

"For Loop in python different collections of items "

friend = ["Jim", "Karen", "kevin"]
for index in friend:
    print(index)

for index in range(len(friend)):
    print(friend[index])

for letter in "Giraffe Academy":
    print(letter)

for indecies in range(10):
    if indecies == 0:
        print(indecies)
    else:
        print("not First")

"Exponent Function"

print(2 ** 3)
"it is 2 raised to power 3"


def raise_to_power(base_num, pow_num):
    result = 1
    for value in range(pow_num):
        result = result * base_num
        return result


print(raise_to_power(3, 2))

"2d lists and loop"

number_grid = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [0]
]

print(number_grid[0][0])

"nested for loop"

for row in number_grid:
    for col in row:
        print(col)

"build a translator"


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
            return translation


print(translate(input("Enter a phrase: ")))

"Comments in python"
# this program is cool
# so we use "#" for comments
# we can also use another method
'''

multiple lines comments 

'''

# catching errors in python try&Except

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print("err")

except ValueError:
    print("Invalid input")

'''
Reading from files

'''

employee_file = open("employees.txt", "r")  # opening file in read mode

print(employee_file.readable())  # returns a boolean value if file is readable or not

print(employee_file.read())  # read and print the whole data in file

print(employee_file.readline())  # it reads the first line of file

print(employee_file.readlines())  # reads all the lines in the file and arrange them in for of array

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

# you can open it in w - write , a - append , r+ - read and write


# writing to files and appending

employee_file = open("employees.txt", "a")
employee_file.write("Toby - Human Resources")
employee_file.write("\n kelly - Customer Service")


employee_file.close()


# writing mode overwrites the existing content inside the file

employee_file = open("Employees1.txt","w")
employee_file.write(" kapil - Project management")
employee_file.close()

employee_file = open("index.html", "w")
employee_file.write("<p>This is HTML </p>")



"Modules and pip"

#Modules are python files that we can import that into current working python file


import  useful_tools

print(useful_tools.roll_dice(10))



"Classes and objects"

from Student import Student
# one Student is reffering to file and another is reffering to class

student1 = Student("Jim", "Business", 3.1, False)
# student1 is an object

print(student1.name)
print(student1.gpa)

student2= Student("Pam", "Art", 2.5, "True")
print(student2.gpa)


"multiple choice quiz"

from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
     answer = input(question.prompt)
     if answer == question.answer:
            score += 1

     print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)



"Object function we can use inside of class to modify objects"



print(student1.on_honor_roll())


"Inheritance"

from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_bbq()

"Python Interpreter is the environment we use to execute python commands  so we use command prompt"












