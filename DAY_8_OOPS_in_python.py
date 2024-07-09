#question 1 
'''Define a simple Car class with attributes for make, model, and year. 
Create an object of this class and print its attributes.
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("nissan", "gtr", "2022")

print("Make :", my_car.make)
print("Model :", my_car.model)
print("Year :", my_car.year)



#question 2
'''Create a Person class with attributes for name and age. 
Add a method to print a greeting message. Create an object and call the method.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person_detail = Person("AMANDEEP SINGH", "19" )

print("My name is : ", person_detail.name)
print("My age is : ", person_detail.age)



#question 3
'''Define a Rectangle class with attributes for length and width. 
Add a method to calculate the area of the rectangle. Create an object and print the area.
'''
class rectangle :
    def __init__(self , length , width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
Rectangle = rectangle(24,15)
print("Area of the rectangle is : ", Rectangle.calculate_area())

#question 4 
'''Create a Student class with attributes for name and grades (a list of numbers). 
Add a method to calculate the average grade. Create an object and print the average grade.
'''
class student :
    def __init__(self, name , grade):
        self.name = name
        self.grade = grade
    def calculate_average(self):
        return sum(self.grade) / len(self.grade)
student1 = student("Amandeep singh", [85,90,78,65,88,59])
print(f"The  average grade of {student1.name} is {student1.calculate_average():.2f}")


#question 5
''' Define a Book class with attributes for title, author, and pages. 
Add a method to display the book's details. Create an object and call the method.
'''
class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
Book1 = book("atomic habits", "James clear", "380")
print("Title : ", Book1.title)
print("author : ", Book1.author)
print("pages : ", Book1.pages)


#question 6 
'''Create a Dog class with attributes for name and breed. Add a method to make 
the dog bark (print a bark message). Create an object and call the method.'''
class Dog :
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} the {self.breed} says : BHAUUU BHAAAUU !!")
My_dog = Dog("buddy", "Husky")
My_dog.bark()


#question 7 
'''Define a BankAccount class with attributes for account number and balance. 
Add methods to deposit and withdraw money. Create an object and test the methods.'''
class bankaccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount :.2f} into account {self.account_number}. New balance : {self.balance :.2f}")
        else:
            print("Invalid deposit amount. please try again.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdrew {amount : .2f} from account {self.account_number}. New balance : {self.balance :.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount. please try again.")
        else :
            print("Insufficient funds. please try again.")
    def get_balance(self):
        return self.balance
account = bankaccount("123456789")
account.deposit(1000)
account.withdraw(500)
account.withdraw(600)
print(f"Final balance: ${account.get_balance():.2f}")


#Question 8
'''Create a Circle class with attributes for radius. 
Add a method to calculate the circumference. Create an object and print the circumference.
'''
class circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * 3.14 * self.radius
Circle = circle(7)
print("Circumference of circle : ", Circle.circumference())

#question 9 
'''Define a Laptop class with attributes for brand and price. 
Add a method to apply a discount to the price. Create an object and test the method.
'''
class laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = int(price)
    def discount(self):
        discount = 20
        discounted_price = self.price - self.price * discount / 100
        return discounted_price
Laptop = laptop("ASUS", "85000")
print(f"Total price of {Laptop.brand} after discount : ", Laptop.discount())

#question 10 
'''Create a Employee class with attributes for name and salary. 
Add a method to give a raise (increase the salary). Create an object and test the method.
'''
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)
    def salary1(self):
        increment = 14
        increase_in_salary = self.salary + self.salary * increment / 100
        return increase_in_salary
increment = employee("AMANDEEP SINGH", "12000")
print(f"increment of {increment.name} this month is : ", increment.salary1())


#question 11
'''Define a Point class with attributes for x and y coordinates. 
Add a method to calculate the distance from another point. Create two objects 
and print the distance between them.
'''
import math
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Create two points
p1 = point(1, 2)
p2 = point(4, 6)

# Calculate and print the distance between them
distance = p1.distance(p2)
print(f"The distance between ({p1.x}, {p1.y}) and ({p2.x}, {p2.y}) is {distance:.2f}")


#Question 12
'''Create a Movie class with attributes for title, director, and release year. 
Add a method to display the movie's information. Create an object and call the method.
'''
class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Release Year: {self.release_year}")

# Create a Movie object
movie = Movie("The Shawshank Redemption", "Frank Darabont", 1994)

# Call the display_info method
movie.display_info()