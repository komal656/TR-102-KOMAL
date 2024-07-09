'''                                                                                                                                                        Question 1: Library Management System
Scenario: You are tasked with developing a library management system where users can borrow and return books.

Requirements:

Create a Book class that has the following private attributes: title, author, and isbn.
Implement methods to get and set the values of these attributes (getters and setters).
Create a Library class that has a list of Book objects.
Implement methods to add a new book, remove a book by its ISBN, and list all available books.
Use encapsulation to ensure that the books can only be manipulated through the Library class.
Task:

Implement the Book and Library classes with proper encapsulation.
Add methods to add, remove, and list books in the library.
'''
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}"


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, isbn):
        for book in self.__books:
            if book.get_isbn() == isbn:
                self.__books.remove(book)
                print(f"Book with ISBN {isbn} removed successfully.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def list_books(self):
        if not self.__books:
            print("No books in the library.")
        else:
            for book in self.__books:
                print(book)


# Example usage:
library = Library()

book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("Pride and Prejudice", "Jane Austen", "9780486280511")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.list_books()

library.remove_book("9780451524935")

library.list_books()


'''Question 2: Bank Account Management
Scenario: Develop a bank account management system where users can create accounts, deposit, and withdraw money.

Requirements:

Create a BankAccount class with private attributes: account_number, account_holder, and balance.
Implement methods to get the account details and balance (getters).
Implement methods to deposit and withdraw money, ensuring that the balance cannot go negative.
Use encapsulation to ensure that the balance cannot be directly modified.
Task:

Implement the BankAccount class with proper encapsulation.
Add methods to deposit and withdraw money, and to get account details.
'''
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ${amount:.2f} successful. New balance: ${self.__balance:.2f}")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.__balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please try again.")
        else:
            print("Insufficient balance. Please try again.")

    def __str__(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: ${self.__balance:.2f}"


# Example usage:
account = BankAccount("1234567890", "John Doe")

print(account)

account.deposit(1000.0)
account.withdraw(500.0)
account.withdraw(600.0)

print(account)


'''Question 3: Employee Management System
Scenario: You are developing an employee management system for a company.

Requirements:

Create an Employee class with private attributes: employee_id, name, position, and salary.
Implement methods to get and set the values of these attributes, with validation on the salary (e.g., salary cannot be negative).
Create a Department class that has a list of Employee objects.
Implement methods to add a new employee, remove an employee by their ID, and list all employees in the department.
Use encapsulation to ensure that employees can only be manipulated through the Department class.
Task:

Implement the Employee and Department classes with proper encapsulation.
Add methods to add, remove, and list employees in the department.
'''
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__position = position
        self.__salary = self.__validate_salary(salary)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = self.__validate_salary(salary)

    def __validate_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        return salary

    def __str__(self):
        return f"Employee ID: {self.__employee_id}, Name: {self.__name}, Position: {self.__position}, Salary: ${self.__salary:.2f}"


class Department:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.__employees:
            if employee.get_employee_id() == employee_id:
                self.__employees.remove(employee)
                print(f"Employee with ID {employee_id} removed successfully.")
                return
        print(f"Employee with ID {employee_id} not found.")

    def list_employees(self):
        if not self.__employees:
            print(f"No employees in the {self.__name} department.")
        else:
            for employee in self.__employees:
                print(employee)


# Example usage:
department = Department("Sales")

employee1 = Employee("E001", "John Doe", "Sales Representative", 50000.0)
employee2 = Employee("E002", "Jane Smith", "Sales Manager", 80000.0)
employee3 = Employee("E003", "Bob Johnson", "Sales Associate", 40000.0)

department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)

department.list_employees()

department.remove_employee("E002")

department.list_employees()


'''Question 4: Online Shopping System
Scenario: Develop an online shopping system where users can add products to a shopping cart and view the total cost.

Requirements:

Create a Product class with private attributes: product_id, name, and price.
Implement methods to get the product details (getters).
Create a ShoppingCart class that has a list of Product objects.
Implement methods to add a product to the cart, remove a product by its ID, and calculate the total cost of all products in the cart.
Use encapsulation to ensure that products in the cart can only be manipulated through the ShoppingCart class.
Task:

Implement the Product and ShoppingCart classes with proper encapsulation.
Add methods to add, remove, and list products in the cart, and to calculate the total cost.
'''
class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = self.__validate_price(price)

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def __validate_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        return price

    def __str__(self):
        return f"Product ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                print(f"Product with ID {product_id} removed successfully.")
                return
        print(f"Product with ID {product_id} not found.")

    def list_products(self):
        if not self.__products:
            print("Your shopping cart is empty.")
        else:
            for product in self.__products:
                print(product)

    def calculate_total_cost(self):
        total_cost = sum(product.get_price() for product in self.__products)
        return total_cost


# Example usage:
cart = ShoppingCart()

product1 = Product("P001", "Apple Watch", 299.99)
product2 = Product("P002", "Samsung TV", 999.99)
product3 = Product("P003", "Nike Shoes", 79.99)

cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.list_products()

print(f"Total cost: ${cart.calculate_total_cost():.2f}")

cart.remove_product("P002")

cart.list_products()

print(f"Total cost: ${cart.calculate_total_cost():.2f}")


'''Question 5: School Management System
Scenario: Develop a school management system where you can manage students and their courses.

Requirements:

Create a Student class with private attributes: student_id, name, and courses (a list of course names).
Implement methods to get and set the student's details and courses (getters and setters).
Create a School class that has a list of Student objects.
Implement methods to add a new student, remove a student by their ID, and list all students and their courses.
Use encapsulation to ensure that students can only be manipulated through the School class.
Task:

Implement the Student and School classes with proper encapsulation.
Add methods to add, remove, and list students and their courses.
'''
class Student:
    def __init__(self, student_id, name, courses=None):
        self.__student_id = student_id
        self.__name = name
        self.__courses = courses if courses is not None else []

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_courses(self):
        return self.__courses

    def set_courses(self, courses):
        self.__courses = courses

    def add_course(self, course):
        self.__courses.append(course)

    def remove_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
        else:
            print(f"Course {course} not found.")

    def __str__(self):
        return f"Student ID: {self.__student_id}, Name: {self.__name}, Courses: {', '.join(self.__courses)}"


class School:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                self.__students.remove(student)
                print(f"Student with ID {student_id} removed successfully.")
                return
        print(f"Student with ID {student_id} not found.")

    def list_students(self):
        if not self.__students:
            print(f"No students in {self.__name} school.")
        else:
            for student in self.__students:
                print(student)


# Example usage:
school = School("Springfield High")

student1 = Student("S001", "Bart Simpson", ["Math", "English", "Science"])
student2 = Student("S002", "Lisa Simpson", ["Math", "English", "Music"])
student3 = Student("S003", "Milhouse Van Houten", ["Math", "English", "Gym"])

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.list_students()

student1.add_course("History")
student2.remove_course("Music")

school.list_students()

school.remove_student("S002")

school.list_students()


'''Question 6: Car Rental System
Scenario: Develop a car rental system where users can rent and return cars.

Requirements:

Create a Car class with private attributes: car_id, make, model, and availability (boolean).
Implement methods to get and set the car's details and availability (getters and setters).
Create a CarRental class that has a list of Car objects.
Implement methods to add a new car, remove a car by its ID, and list all available cars.
Implement methods to rent a car (set its availability to False) and return a car (set its availability to True).
Use encapsulation to ensure that cars can only be manipulated through the CarRental class.
Task:

Implement the Car and CarRental classes with proper encapsulation.
Add methods to add, remove, list, rent, and return.cars.'''
class Car:
    def __init__(self, car_id, make, model, availability=True):
        self.__car_id = car_id
        self.__make = make
        self.__model = model
        self.__availability = availability

    def get_car_id(self):
        return self.__car_id

    def set_car_id(self, car_id):
        self.__car_id = car_id

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_availability(self):
        return self.__availability

    def set_availability(self, availability):
        self.__availability = availability

    def __str__(self):
        return f"Car ID: {self.__car_id}, Make: {self.__make}, Model: {self.__model}, Availability: {self.__availability}"


class CarRental:
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        self.__cars.append(car)

    def remove_car(self, car_id):
        for car in self.__cars:
            if car.get_car_id() == car_id:
                self.__cars.remove(car)
                print(f"Car with ID {car_id} removed successfully.")
                return
        print(f"Car with ID {car_id} not found.")

    def list_available_cars(self):
        available_cars = [car for car in self.__cars if car.get_availability()]
        if not available_cars:
            print("No cars available for rent.")
        else:
            for car in available_cars:
                print(car)

    def rent_car(self, car_id):
        for car in self.__cars:
            if car.get_car_id() == car_id:
                if car.get_availability():
                    car.set_availability(False)
                    print(f"Car with ID {car_id} rented successfully.")
                    return
                else:
                    print(f"Car with ID {car_id} is not available for rent.")
                    return
        print(f"Car with ID {car_id} not found.")

    def return_car(self, car_id):
        for car in self.__cars:
            if car.get_car_id() == car_id:
                if not car.get_availability():
                    car.set_availability(True)
                    print(f"Car with ID {car_id} returned successfully.")
                    return
                else:
                    print(f"Car with ID {car_id} is already available for rent.")
                    return
        print(f"Car with ID {car_id} not found.")


# Example usage:
rental = CarRental()

car1 = Car("C001", "Toyota", "Corolla")
car2 = Car("C002", "Honda", "Civic")
car3 = Car("C003", "Ford", "Focus")

rental.add_car(car1)
rental.add_car(car2)
rental.add_car(car3)

rental.list_available_cars()

rental.rent_car("C001")

rental.list_available_cars()

rental.return_car("C001")

rental.list_available_cars()

rental.remove_car("C002")

rental.list_available_cars()