# Dictionary
"""
Dictionaries are ordered ,changable but do not allow duplicates 
-used to store data values in key:values pairs
-they can have items of any data type
"""

mydict = {"phone": "iphone", "model": "iphone15", "year": 2023}
print(mydict)

# length
print(len(mydict))
# data type
print(type(mydict))
# Access
z = mydict["year"]
print(z)
print(mydict["phone"])
y = mydict.get("model")
print(y)
w = mydict.keys()
print(w)  # prints out all the keys ie. phone, model, year

# My example
# Creating a dictionary
student = {
    "name": "Laura ",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Science", "English"],
}

# Accessing dictionary values
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])
print("Courses:", student.get("courses"))

# keys
print(student.keys())
# Modifying dictionary values
student["age"] = 21
student["courses"].append("History")  # addes value to existing key

# Adding a new key-value pair
student["address"] = "Luzira"

"""
Deleting a key-value pair
del student["grade"]
"""

# exercise 1: use value()- lists of all vlaues int he dictionary
print(student.values())
# Exercise 2 : Check if a key exists
if "name" in student:
    print("Name key exists")
if "college" in student:
    print("College key exists")
else:
    print("key does not exist")
# Excerise 3:How to change dictionary items and how to update
student["name"] = "Lorna"
student.update({"grade": "B+"})
# Excerise 4:how to add dictionary items, how to remove items
student["courses"].append("History")
del student["courses"]
# Exercise 5: loop through dictionary and nested dictionaries
for key in student:
    print(key, ":", student[key])

# nested dictionaries
student = {
    "name": "Laura ",
    "age": 21,
    "grade": "A",
    "courses": ["Math", "Science", "English"],
    "address": {
        "city": "Luzira",
        "country": "Uganda",
    },
}

# Numbers
# integers,floats,complex
w = 60  # int
t = 3.14  # float
r = 12j  # complex
print(type(w))
print(type(t))
print(type(r))

"""
Integers- whole numbers,negative or positive,no decimals , unlimited length
 
Floats-is a number, positive or negative, containing one or more decimals places
 -Float can also be scientific numbers with an "e" to indicate the power of 10

Complex-They are numbers that are written with a "j" as the imaginary part:
ie x=3+5j
y=5j
z=-5j
"""

# Conversion
a = float(w)  # int to float
b = complex(t)  # float to complex
# c = float(r)  # complex to float NB:Impossible float must be a real number
print(a, b)
# print(c) not possible
print(type(a))
print(type(b))
# print(type(c)) not possible

# Typecasting
# works mostly when you want to specify a variable type

# int
l = int("40")
m = int(560)
print(type(l))  # output- 40

# string
q = str(30)
d = str(5j)
print(type(q))
print(type(d))

# float
o = float("0.0")
i = float(1)
print(type(o))
print(type(i))

# STRING
print("afternoon")
print("afternoon")
# they are the same, depends on preference
print("afternoon" == "afternoon")
print("afternoon" == "afternoon")

# assigning string to a variable
y = "everything"
print(y)

# Multiline string
z = """
This is a multiline string.
The quick brown fox jumped over the lazy dog.
"""
print(z)

r = """ 
A random paragraph can also be an excellent way 
for a writer to tackle writers' block. 
Writing block can often happen due to being 
stuck with a current project that the writer is 
trying to complete.
"""
print(r)

# string as array
e = "Everything"
print(e[3])  # output- r

# Excerise 1- use len()
print(len(e))
# Excersie 2-example of loop in a string
for i in e:
    print(i)
# Excerise 3- example of slicing stings
j = "Hello my name is Laura"
print(j[0:5])  # characters from post 2 to 5 (not included)
print(j[5:])  # characters from post5 to end
print(j[:5])  # characters from start to post 5 (not included)
print(j[-6:-2])  # characters from post -6 to -2

# modify string
print(e.lower())  # lowercase string
print(e.upper())  # uppercase string
print(e.capitalize())  # capitalize string
print(e.title())  # title case string
print(e.swapcase())  # swap case string
print(e.count("e"))  # count number of e in string
print(e.find("e"))  # find position of e in string
print(e.replace("e", "E"))  # replace e with E in string
print(e.index("e"))  # find position of e in string
print(e.count("e"))  # count number of e in string
print(e.find("e"))  # find position of e in string

# remove whitespace
s = " lunch times "
print(s.strip())  # remove whitespace
print(s.lstrip())  # remove whitespace from left
print(s.rstrip())  # remove whitespace from right

# Concantination
print(e + e)
print(e * 3)
c = "hi"
f = "friends"
print(c + f)
k = c + " " + f
print(k)


# FORMAT STRINGS
# Works when one wants to combine a string to a number
# use need to use format method ie format()
# then within string put in the placeholders {} for where the the method can put in the interger

age = 21
"""
name="My name is Laura" + age
print(name) #no longer works 
"""
name = "My name is laura, i am {}"
print(name.format(age))

# Multiple *placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# BOOLEAN
# evalute to true or false
print(20 < 10)
print(30 > 20)
print(50 == 40)
"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""
print(bool(4565))
print(bool(""))
print(bool(0))
print("laura")
print(bool([]))

# Exercise 1:use a condition to show how to use booleans
if 20 < 10:
    print("20 is less than 10")
if 30 > 20:
    print("30 is greater than 20")
if 50 == 40:
    print("50 is equal to 40")
else:
    print("Error")
