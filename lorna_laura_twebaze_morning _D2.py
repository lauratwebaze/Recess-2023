# Control Flow Statements in Python
"""
If Statement:
The if statement allows you to execute a code block if a certain condition is true. It provides the 
ability to make decisions in your code based on different conditions. You can use elif to check
additional conditions, and else to specify a code block when none of the conditions are true.
"""
a = 33
b = 200
if b > a:
    print("b is greater than a")

# elif & else
age = int(input("Enter age:"))
if age < 18:
    print("You are underage")
elif age >= 18 and age < 65:
    print("you are an adult")
else:
    print("you are a senior citizen")

# and
n = 200
v = 33
y = 500
if n > v and y > n:
    print("Both conditions are True")

# or
o = 200
p = 33
i = 500
if o > p or o > i:
    print("At least one of the conditions is True")

# not
aa = 43
bb = 300
if not aa > bb:
    print("a is NOT greater than b")

# nested if
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# For Loop:
# The for loop is used to iterate over a sequence or iterable object. It allows you to execute a code
# block for each item in the sequence. This loop is useful when you want to perform a repetitive task
# for a specific number of times or go through each element in a collection.

cars = ["tesla", "jeep", "ford", "toyota", "BMW"]
for car in cars:
    print(car)

fruits = ["grapes", "apples", "kiwi", "mango"]
for fruit in fruits:
    print(fruit)

for x in "Twebaze":
    print(x)


# While Loop:
# The while loop executes a code block as long as a certain condition remains true. It repeatedly
# checks the condition before each iteration.It is helpful when you need to perform a task
# until a specific condition is met or until a certain event occurs.

fruits_count = 0
while fruits_count < len(fruits):
    print(fruits_count)
    fruits_count += 1

xx = 0
while xx < 10 and xx > 2:
    print(xx)
    if x == 8:
        break
xx += 1


# Break Statement:
# The break statement is used to exit a loop prematurely.
# When a break statement is encountered, the loop is immediately terminated,
# even if the loop condition is still true. It is often used to stop the execution of
# a loop based on a certain condition.

# break terminates loop

for number in range(1, 8):
    if number == 4:
        break
    print(number)

# Continue Statement:
# The continue statement allows you to skip the current iteration
#  of a loop and move to the next iteration. When the continue statement
#  is encountered, the remaining code in the loop for the current iteration is skipped,
#  and the loop proceeds with the next iteration.

# continue skips the number

for number in range(1, 8):
    if number == 4:
        continue
print(number)

# Pass Statement:
# The pass statement is a placeholder that does nothing.
# It is used when a statement is required syntactically but you don't want to perform any action.

#  It is commonly used as a placeholder for future code or when an empty block is needed.
# If statements cannot be empty,but if you for some reason have an if statement
# with no content, put in the pass statement to avoid getting an error

ap = 33
bp = 200

if bp > ap:
    pass

# Try-Except Statement:
# The try-except statement is used to handle exceptions (errors) that may
# occur during the execution of code. The try block contains the code that may raise an exception.
# If an exception occurs, it is caught by the corresponding except block, allowing you to handle the exception
# gracefully. The else block is executed if no exceptions are raised, and the finally block is always executed,
# regardless of whether an exception occurred or not.

# Exception handling(try,except, finally)

try:
    x = 10 / 0
except ZeroDivisionError:
    print("error: cant be divided by zero")
finally:
    print("this is always divided")

# example
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Exercise 1
# Prompting  a student to enter their mental health rating
health = {
    1: "Im in emotional duress",
    2: "Im at a critical point",
    3: "Im struggling to cope",
    4: "Im overwhelmed",
    5: "Im mental health is greatly impacting my everyday life",
    6: "My mental health is impacting my everyday life",
    7: "Im feeling averagely low",
    8: "Im a little bit stressed/annoyed",
    9: "Im okay",
    10: "Im very good",
}

# prompt
name = input("Please enter your name:")
print(health)
while (
    True
):  # a while loop is used to repeatedly prompt the user until a valid rating is entered.
    try:
        user_health = int(
            input(
                "Based on range above, please enter your current mental health rating:"
            )
        )

        if user_health < 1 or user_health > 10:
            print("Invalid rating. Please enter a number between 1 and 10.")
        else:
            print("Thank you for sharing your mental health rating!")
            break  # Exit the loop if a valid rating is entered
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if 7 <= user_health <= 10:
    print(
        f"Well Done {name}! Your mental health rating was {user_health}, which is good/mild. Please keep this up! Endevour to journal to keep track."
    )
if 4 <= user_health <= 6:
    print(
        f"Hi {name},I hope you are okay. Your mental health rating was {user_health}, which is moderate.Please consider self care and look after your self.Maybe consider seeing a professional."
    )
if 1 <= user_health <= 3:
    print(
        f"Hello {name},I am very worried about you. Your mental health rating was {user_health}, which is servere. Please seek help from a mental health professional immediately.Here is a helpline which might help: 0800212121"
    )
