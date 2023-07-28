# example 1
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine has started")

    def stop_engine(self):
        print("Engine stopped")


# create object
my_car = Car("Toyota", "Corola", 2022)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()


object


class Person:
    def __init__(
        self, name, age, course
    ):  # two underscores for init function to that intializes
        self.name = name
        self.age = age
        self.course = course

    def greet(self):
        print("hello, my name is", self.name)
        print("i am ", self.age, " years old")
        print("i am studying ", self.course)


# Person object
my_person = Person("laura", 21, "Software Engineering")
my_person1 = Person("natasha", 26, "Law")

# invoke

my_person.greet()


# exercise 1 circle
class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * (self.radius * self.radius)

    def calculate_circumference(self):
        return 2 * 3.14159 * (self.radius)


my_circle = circle(7)
print(my_circle.radius)
print(my_circle.calculate_area())
print(my_circle.calculate_circumference())


# example 1.b Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# create a rectangle
my_rectangle = Rectangle(15, 5)
print(my_rectangle.length)
print(my_rectangle.width)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())


# Exercise 2
# calculate employee bonuses (0.15) of salary


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.15


e1 = Employee("laura ", 150000)
e2 = Employee("natasha ", 230000)

print(e2.name + "your bonus is:" + str(e2.bonus()))
print(e1.name + "your bonus is:" + str(e1.bonus()))

# encapsulation
# Main goals of encapsulation are
"""
1. To hide the implementation details of an object from other objects.
2. To protect the object from changes 
3.To protect the object from external changes
4.Code oragnization and modularity
"""


# Example 4 : bank account
class BankAccount(object):
    def __init__(self, _account_number, _balance):
        self._account_number = _account_number  # Encapsulates the account number attribute- Basically a unique name that would be hard to hack

        self._balance = _balance  # Encapsulates the balance attribute

    def deposit(self, amount):
        self._balance += amount  # encapsulates the deposit amount attribute

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print("withdraw amount", amount, "balance:", self._balance)
        else:
            print("insufficient balance")

    def get_balance(self):
        return self._balance


# Bank Object
my_account = BankAccount("234737376364", 1000)

# accessing accounts
my_account.get_balance()
my_account.deposit(500)
my_account.get_balance()
my_account.withdraw(500)
my_account.get_balance()


# exercise 5:Covert temperature (37 c) from celsius to fahrenheit


class Temperature:
    def __init__(self, _celsius):
        self._celsius = _celsius

    def _fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


temp = Temperature(37)
converted = temp._fahrenheit()
print(f"The Temperature {temp._celsius} Celsius is conveted to {converted} fahrenheit")


# assignment 1:Show encapsulation empoyee infomation to give a  pay increament
# (salary with employee information to new_salaryeg 850000 to 1000000)
# next lesson=> polymorhism and absraction


class Employee:
    def __init__(self, name, employee_id, salary):
        self._name = name
        self._employee_id = employee_id
        self._salary = salary

    def get_name(self):
        return self._name

    def get_employee_id(self):
        return self._employee_id

    def get_salary(self):
        return self._salary

    def give_pay_increment(self, increment_amount):
        self._salary += increment_amount


# Creating an employee object
employee = Employee("Laura Twebaze", 12345, 850000)

# Displaying the current salary
print("Employee Information:")
print("Name:", employee.get_name())
print("Employee ID:", employee.get_employee_id())
print("Current Salary:", employee.get_salary())

# Giving a pay increment
increment_amount = 150000
employee.give_pay_increment(increment_amount)

# Displaying the updated salary
print("\nAfter Pay Increment:")
print("New Salary:", employee.get_salary())
