# Exercise 1 - Lists
print("Exercise 1-lists")
# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
name = ["laura", "lorna", "cronnie", "lynn", "bob"]
print(name[1])

# 2. Write a python program to change the value of the first item to a new value
name[1] = "trisha"

# 3. Write a python program to add a sixth item to the list
name.append("Emma")

# 4. Write a python program to add “Bathel” as the 3rd item in your list
name.insert(2, "Bethel")

# 5. Write a python program to remove the 4th item from the list
name.pop(3)

# 6. Use negative indexing to print the last item in your list
print(name[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:5])  # such that the 5th item is included

# 8. Write a list of countries and make a copy of it.
countries = ["Uganda", "India", "USA", "Fiji"]
x = countries.copy()

# 9. Write a python program to loop through the list of countries
for x in countries:
    print(x)

# 10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["elephant", "cow", "ant", "dog", "baboon"]
print(animals)
animals.sort()
print(animals)
animals.sort(reverse=True)
print(animals)

# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
for name in animals:
    if "a" in name.lower():
        print(name)

# 12. Write two lists, one containing your first names and the other your second names. Join the two lists
first_names = ["Lorna", "Laura", "Luna", "Emily"]
last_names = ["Twebaze", "Musimenta", "Agaba", "Kukunda"]

full_names = []

for i in range(len(first_names)):
    full_name = first_names[i] + " " + last_names[i]
    full_names.append(full_name)

print(full_names)

# Exercise 2
print("Exercise 2 -Tuples")
# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[2]
print("My favorite phone brand is:", favorite_phone_brand)

# 2. Use negative indexing to print the 2nd last item in your tuple.
print(x[-2])

# 3. Using the phones list above, write a python program to update “iphone” to “itel”
x = ("samsung", "iphone", "tecno", "redmi")
y = list(x)
y[1] = "Itel"
x = tuple(y)
print(x)

# 4. Write a python program to add “Huawei” to your tuple.
y = list(x)
y.append("Huawei")
x = tuple(y)
print(x)

# 5. Write a python program to loop through the tuple above.
for items in x:
    print(items)

# 6. Write a python program to remove/delete the first item in your tuple.
y = list(x)
y.pop(0)
x = tuple(y)
print(x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(cities)

# 8. Write a python program to unpack your tuple.
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
city1, city2, city3, city4, city5 = cities

print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)
print("City 5:", city5)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print(cities[1:4])  # such that the 4th item is included

# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
tuple1 = ("Jo", "Bob", "Cath")
tuple2 = ("Brown", "Yu", "Kato")

tuple3 = tuple1 + tuple2
print(tuple3)

# 11. Create a tuple of colors and multiply it by 3.
colour = ("blue", "yellow", "red")
mytuple = colour * 3
print(mytuple)

# 12. Return the number of times 8 appears in this tuple thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)

# Exercise 3- sets
print("Exercise 3-Sets")
# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
drink = set(("coke", "water", "juice"))

# 2. Use the correct method to add 2 more items to the beverages set.
drink.add("tea")
drink.add("redbull")  # since add method takes one argument
print(drink)
# 3. Given the set below;
# mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
# Check if microwave is present in the set.
mySet = {"oven", "kettle", "mircowave", "refrigerator"}
if "mircowave" in mySet:
    print("Microwave is present")
# 4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print(mySet)
# 5. Write a python program to loop through the set above.
for x in mySet:
    print(x)
# 6. Write a set of 4 items and a list of two items.
# Write a python program to add elements in the list to elements in the set.
my_set = {1, 2, 3, 4}
my_list = [5, 6]
m = set(my_list)
combined_set = my_set.union(m)
print("Combined Set:", combined_set)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 35}
first_names = {"John", "Jane", "Michael"}

combined_set = ages.union(first_names)

print(combined_set)

# Exercise 4- Strings
print("Exercise 4-Strings")
# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
num = 56
text = "hi"
concatenate = str(num) + text
print(concatenate)

# 2. Consider the example below;
# txt = “ Hello, Uganda! ”
# Output the string without spaces at the beginning, in the middle and at the end.
txt = "  Hello,  Uganda!  "
txt_without_spaces = txt.strip()
txt_without_spaces = txt_without_spaces.replace(" ", "")

print(txt_without_spaces)

# 3. Write a python program to convert the value of ‘txt’ to uppercase.
print(txt.upper())

# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
print(txt.replace("U", "V"))

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
# y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
print(y[1:5])

# 6. The piece of code below will give an error when output;
# x = “All “Data Scientists” are cool!”
# Write a python program to correct it
x = 'All "Data Scientists" are cool!'

# Exercise 5-Dictionaries
print("Exercise 5->Dictionaries")
# 1. With reference to the dictionary below, write a python program to print the value of the shoe size.Add this dictionary to your .py file
# Shoes = {
# “brand” : “Nick”,
# “color” : “black”,
# “size” : 40}
Shoes = {"brand": "Nike", "color": "black", "size": 40}

shoe_size = Shoes["size"]

print("Shoe Size:", shoe_size)

# 2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)

# 3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"

# 4. Write a python program to return a list of all the keys in the dictionary above.
u = Shoes.keys()
print(u)

# 5. Write a python program to return a list of all the values in the dictionary above.
t = Shoes.values()
print(t)

# 6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("size is present")
else:
    print("size is not present")

# 7. Write a python program to loop through the dictionary above.
for x, y in Shoes.items():
    print(x, ":", y)

# 8. Write a python program to remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)
# 9. Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)
# 10. Write a dictionary of your choice and make a copy of it.
student = {"name": "Eugene", "dob": "2.03.2002", "age": 21}
pupil = student.copy()
print(pupil)

# 11. Write a python program to show nested dictionaries
college = {
    "student1": {"name": "Emily", "graduates": 2025, "dob": "2.03.2002", "age": 21},
    "student2": {"name": "Tobias", "graduates": 2026, "dob": "2.03.2003", "age": 20},
    "student3": {"name": "Linus", "graduates": 2024, "dob": "2.03.2001", "age": 22},
}
print(college)
