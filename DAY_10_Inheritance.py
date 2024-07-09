'''1. Smart Home Automation System
Question: Design a smart home automation system. Create a base class Device with common attributes like device_id, name, and methods like turn_on and turn_off. Create derived classes Light, Thermostat, and SecurityCamera with specific attributes and methods. Implement polymorphism to handle different devices.

Requirements:

Device class with device_id, name, turn_on(), and turn_off().
Light class with brightness and color attributes.
Thermostat class with temperature attribute and set_temperature() method.
SecurityCamera class with resolution attribute and record() method.
Use polymorphism to iterate over a list of devices and call their specific methods.'''
class Device:
    def __init__(self, device_id, name):
        self.__device_id = device_id
        self.__name = name
        self.__is_on = False

    def get_device_id(self):
        return self.__device_id

    def get_name(self):
        return self.__name

    def turn_on(self):
        self.__is_on = True
        print(f"{self.__name} is turned on.")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.__name} is turned off.")

    def __str__(self):
        return f"Device ID: {self.__device_id}, Name: {self.__name}, Status: {'On' if self.__is_on else 'Off'}"


class Light(Device):
    def __init__(self, device_id, name, brightness, color):
        super().__init__(device_id, name)
        self.__brightness = brightness
        self.__color = color

    def get_brightness(self):
        return self.__brightness

    def set_brightness(self, brightness):
        self.__brightness = brightness

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def __str__(self):
        return f"Light - {super().__str__()}, Brightness: {self.__brightness}, Color: {self.__color}"


class Thermostat(Device):
    def __init__(self, device_id, name, temperature):
        super().__init__(device_id, name)
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f"Temperature set to {temperature} degrees.")

    def __str__(self):
        return f"Thermostat - {super().__str__()}, Temperature: {self.__temperature} degrees"


class SecurityCamera(Device):
    def __init__(self, device_id, name, resolution):
        super().__init__(device_id, name)
        self.__resolution = resolution

    def get_resolution(self):
        return self.__resolution

    def set_resolution(self, resolution):
        self.__resolution = resolution

    def record(self):
        print(f"Recording video at {self.__resolution} resolution.")

    def __str__(self):
        return f"Security Camera - {super().__str__()}, Resolution: {self.__resolution}"


# Example usage:
devices = [
    Light("L001", "Living Room Light", 50, "White"),
    Thermostat("T001", "Living Room Thermostat", 22),
    SecurityCamera("SC001", "Front Door Camera", "HD")
]

for device in devices:
    print(device)
    device.turn_on()
    if isinstance(device, Light):
        device.set_brightness(75)
        device.set_color("Yellow")
    elif isinstance(device, Thermostat):
        device.set_temperature(25)
    elif isinstance(device, SecurityCamera):
        device.record()
    print(device)
    device.turn_off()
    print(device)
    print()



'''2. Employee Management System
Question: Develop an employee management system. Create a base class Employee with attributes like name, id, and salary. Create derived classes Manager, Developer, and Designer with specific attributes and methods. Implement method overriding and class-specific behavior.

Requirements:

Employee class with name, id, salary, and display_details() method.
Manager class with team_size attribute and conduct_meeting() method.
Developer class with programming_languages attribute and write_code() method.
Designer class with design_tools attribute and create_design() method.
Override display_details() in each subclass to include specific details.'''
class Employee:
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_salary(self):
        return self.__salary

    def display_details(self):
        print(f"Employee ID: {self.__id}, Name: {self.__name}, Salary: ${self.__salary:.2f}")


class Manager(Employee):
    def __init__(self, name, id, salary, team_size):
        super().__init__(name, id, salary)
        self.__team_size = team_size

    def get_team_size(self):
        return self.__team_size

    def conduct_meeting(self):
        print(f"{self.get_name()} is conducting a meeting with their team of {self.__team_size} members.")

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.__team_size}")


class Developer(Employee):
    def __init__(self, name, id, salary, programming_languages):
        super().__init__(name, id, salary)
        self.__programming_languages = programming_languages

    def get_programming_languages(self):
        return self.__programming_languages

    def write_code(self):
        print(f"{self.get_name()} is writing code in {', '.join(self.__programming_languages)}.")

    def display_details(self):
        super().display_details()
        print(f"Programming Languages: {', '.join(self.__programming_languages)}")


class Designer(Employee):
    def __init__(self, name, id, salary, design_tools):
        super().__init__(name, id, salary)
        self.__design_tools = design_tools

    def get_design_tools(self):
        return self.__design_tools

    def create_design(self):
        print(f"{self.get_name()} is creating a design using {', '.join(self.__design_tools)}.")

    def display_details(self):
        super().display_details()
        print(f"Design Tools: {', '.join(self.__design_tools)}")


# Example usage:
employees = [
    Manager("John Doe", "M001", 100000, 10),
    Developer("Jane Smith", "D001", 80000, ["Python", "Java", "C++"]),
    Designer("Bob Johnson", "D002", 70000, ["Adobe Photoshop", "Sketch", "Figma"])
]

for employee in employees:
    employee.display_details()
    if isinstance(employee, Manager):
        employee.conduct_meeting()
    elif isinstance(employee, Developer):
        employee.write_code()
    elif isinstance(employee, Designer):
        employee.create_design()
    print()




'''3. E-Learning Platform
Question: Create an e-learning platform. Design a base class Course with common attributes like course_id, title, and methods like enroll_student and unenroll_student. Create derived classes ProgrammingCourse, DesignCourse, and MathCourse with specific attributes and methods.

Requirements:

Course class with course_id, title, students, enroll_student(), and unenroll_student().
ProgrammingCourse class with languages attribute and start_project() method.
DesignCourse class with software attribute and assign_design_task() method.
MathCourse class with difficulty_level attribute and assign_homework() method.
Use polymorphism to manage courses and their specific tasks.
'''
class Course:
    def __init__(self, course_id, title):
        self.__course_id = course_id
        self.__title = title
        self.__students = []

    def get_course_id(self):
        return self.__course_id

    def get_title(self):
        return self.__title

    def get_students(self):
        return self.__students

    def enroll_student(self, student):
        self.__students.append(student)
        print(f"{student} has been enrolled in {self.__title}.")

    def unenroll_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            print(f"{student} has been unenrolled from {self.__title}.")
        else:
            print(f"{student} is not enrolled in {self.__title}.")


class ProgrammingCourse(Course):
    def __init__(self, course_id, title, languages):
        super().__init__(course_id, title)
        self.__languages = languages

    def get_languages(self):
        return self.__languages

    def start_project(self):
        print(f"Starting a programming project in {', '.join(self.__languages)} for {self.get_title()}.")

    def display_details(self):
        print(f"Course ID: {self.get_course_id()}, Title: {self.get_title()}, Languages: {', '.join(self.__languages)}")


class DesignCourse(Course):
    def __init__(self, course_id, title, software):
        super().__init__(course_id, title)
        self.__software = software

    def get_software(self):
        return self.__software

    def assign_design_task(self):
        print(f"Assigning a design task using {self.__software} for {self.get_title()}.")

    def display_details(self):
        print(f"Course ID: {self.get_course_id()}, Title: {self.get_title()}, Software: {self.__software}")


class MathCourse(Course):
    def __init__(self, course_id, title, difficulty_level):
        super().__init__(course_id, title)
        self.__difficulty_level = difficulty_level

    def get_difficulty_level(self):
        return self.__difficulty_level

    def assign_homework(self):
        print(f"Assigning homework with a difficulty level of {self.__difficulty_level} for {self.get_title()}.")

    def display_details(self):
        print(f"Course ID: {self.get_course_id()}, Title: {self.get_title()}, Difficulty Level: {self.__difficulty_level}")


# Example usage:
courses = [
    ProgrammingCourse("PC001", "Python Programming", ["Python", "JavaScript"]),
    DesignCourse("DC001", "Graphic Design", "Adobe Photoshop"),
    MathCourse("MC001", "Calculus", "Advanced")
]

for course in courses:
    course.display_details()
    course.enroll_student("John Doe")
    course.enroll_student("Jane Smith")
    if isinstance(course, ProgrammingCourse):
        course.start_project()
    elif isinstance(course, DesignCourse):
        course.assign_design_task()
    elif isinstance(course, MathCourse):
        course.assign_homework()
    print()



'''4. Restaurant Management System
Question: Design a restaurant management system. Create a base class Restaurant with common attributes like name, location, and methods like open_restaurant and close_restaurant. Create derived classes FastFoodRestaurant, FineDiningRestaurant, and Cafe with specific attributes and methods.

Requirements:

Restaurant class with name, location, open_restaurant(), and close_restaurant().
FastFoodRestaurant class with drive_thru attribute and serve_fast_food() method.
FineDiningRestaurant class with dress_code attribute and serve_gourmet_dishes() method.
Cafe class with coffee_types attribute and serve_coffee() method.
Override open_restaurant() and close_restaurant() in each subclass.'''
class Restaurant:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def open_restaurant(self):
        print(f"{self.__name} at {self.__location} is now open.")

    def close_restaurant(self):
        print(f"{self.__name} at {self.__location} is now closed.")


class FastFoodRestaurant(Restaurant):
    def __init__(self, name, location, drive_thru):
        super().__init__(name, location)
        self.__drive_thru = drive_thru

    def get_drive_thru(self):
        return self.__drive_thru

    def serve_fast_food(self):
        print(f"Serving fast food at {self.get_name()}.")

    def open_restaurant(self):
        super().open_restaurant()
        if self.__drive_thru:
            print("Drive-thru is now open.")

    def close_restaurant(self):
        super().close_restaurant()
        if self.__drive_thru:
            print("Drive-thru is now closed.")


class FineDiningRestaurant(Restaurant):
    def __init__(self, name, location, dress_code):
        super().__init__(name, location)
        self.__dress_code = dress_code

    def get_dress_code(self):
        return self.__dress_code

    def serve_gourmet_dishes(self):
        print(f"Serving gourmet dishes at {self.get_name()}.")

    def open_restaurant(self):
        super().open_restaurant()
        print(f"Please adhere to the {self.__dress_code} dress code.")

    def close_restaurant(self):
        super().close_restaurant()
        print("Thank you for dining with us.")


class Cafe(Restaurant):
    def __init__(self, name, location, coffee_types):
        super().__init__(name, location)
        self.__coffee_types = coffee_types

    def get_coffee_types(self):
        return self.__coffee_types

    def serve_coffee(self):
        print(f"Serving {', '.join(self.__coffee_types)} at {self.get_name()}.")

    def open_restaurant(self):
        super().open_restaurant()
        print(f"Today's coffee specials: {', '.join(self.__coffee_types)}")

    def close_restaurant(self):
        super().close_restaurant()
        print("Come back for your daily dose of caffeine!")


# Example usage:
restaurants = [
    FastFoodRestaurant("Burger King", "New York", True),
    FineDiningRestaurant("The Capital Grille", "Los Angeles", "Formal"),
    Cafe("Starbucks", "Chicago", ["Latte", "Cappuccino", "Mocha"])
]

for restaurant in restaurants:
    restaurant.open_restaurant()
    if isinstance(restaurant, FastFoodRestaurant):
        restaurant.serve_fast_food()
    elif isinstance(restaurant, FineDiningRestaurant):
        restaurant.serve_gourmet_dishes()
    elif isinstance(restaurant, Cafe):
        restaurant.serve_coffee()
    restaurant.close_restaurant()
    print()



'''5. Hospital Management System
Question: Develop a hospital management system. Create a base class Person with common attributes like name, age, and methods like display_info. Create derived classes Doctor, Nurse, and Patient with specific attributes and methods. Implement polymorphism and method overriding.

Requirements:

Person class with name, age, and display_info().
Doctor class with specialization attribute and diagnose() method.
Nurse class with shift attribute and assist() method.
Patient class with ailment attribute and receive_treatment() method.
Override display_info() in each subclass to include specific details.'''
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def diagnose(self):
        print(f"Diagnosing patients with {self.__specialization} expertise.")

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.__specialization}")


class Nurse(Person):
    def __init__(self, name, age, shift):
        super().__init__(name, age)
        self.__shift = shift

    def get_shift(self):
        return self.__shift

    def assist(self):
        print(f"Assisting doctors during {self.__shift} shift.")

    def display_info(self):
        super().display_info()
        print(f"Shift: {self.__shift}")


class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.__ailment = ailment

    def get_ailment(self):
        return self.__ailment

    def receive_treatment(self):
        print(f"Receiving treatment for {self.__ailment}.")

    def display_info(self):
        super().display_info()
        print(f"Ailment: {self.__ailment}")


# Example usage:
hospital_staff = [
    Doctor("Dr. Smith", 35, "Cardiology"),
    Nurse("Nurse Johnson", 28, "Day Shift"),
    Patient("John Doe", 40, "Heart Disease")
]

for staff in hospital_staff:
    staff.display_info()
    if isinstance(staff, Doctor):
        staff.diagnose()
    elif isinstance(staff, Nurse):
        staff.assist()
    elif isinstance(staff, Patient):
        staff.receive_treatment()
    print()