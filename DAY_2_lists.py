#QUESTION 1
'''colors = ['red', 'blue', 'green', 'yellow']
Using the colors list defined above, print the:
First element, Second element, Last element, Second-to-last element, 
Second and third elements, Element at index 4.'''
colors = ["red","blue", "green", "yellow"]
print( "FIRST ELEMENT : ", colors[0])
print("SECOND ELEMENT : ", colors[1])
print("THIRD ELEMENT : ", colors[2])
print("FOURTH ELEMENT : ", colors[3])
print("SECOND-TO-LAST ELEMENT : ", colors[-2]) 
print("SECOND AND THIRD ELEMENT : ", colors[1:3])
#print("ELEMENT AT INDEX 4 :" , colors[4]) #error 


#QUESTION 2
'''Below is a list with seven integer values representing the daily water level (in cm) 
in an imaginary lake. However, there is a mistake in the data. The third day’s water level 
should be 693. Correct the mistake and print the changed list.
water_level = [730, 709, 682, 712, 733, 751, 740]'''
water_level=[730,709,682,712,733,751,740]
water_level.remove(682)
water_level.insert(2,693)
print(water_level)


#QUESTION 3
'''Add the data for the eighth day to the list from above.
The water level was 772 cm on that day. 
Print the list contents afterwards.'''
water_level.append(722)
print(water_level)


#QUESTION 4
'''Still using the same list, add three consecutive days using a single instruction. 
The water levels on the 9th through 11th days were 772 cm, 770 cm, and 745 cm. 
Add these values and then print the whole list.'''
water_level1 = [722,770,745]
water_level.extend(water_level1)
print(water_level)


#QUESTION 5 
'''There are two ways to delete data from a list: by using the index or by using the value. 
Start with the original water_level list we defined in the second exercise and delete the first element using its index. 
Then define the list again and delete the first element using its value.'''
# Original water_level list
water_level = [10, 20, 30, 40, 50]
# Delete the first element using its index
del water_level[0]
# Print the updated list
print("Updated water_level list:", water_level)


#.....  TUPLE  .....
#1 CREATING A TUPLE 
colors = ('red' , 'green', 'blue' )
#Access the second element of the tuple and print it
print(colors[1])


#2 WHY TUPLE ARE CONSIDERED IMMUTABLE :
'''We can't change the elements of a tuple,
but we can execute a variety of actions on them such
as count, index, type, etc.'''
value = 'yellow'
print("Value to be added : ", value )
colors1 = (' yellow ' , )
colors2 = colors + colors1
print("updated tuple is : ", colors2)


#3 Given the tuple numbers = (1, 2, 3, 4, 5) , 
# use slicing to extract the elements from index 1 to 3 (inclusive)
numbers = (1, 2, 3, 4, 5)
extracted_elements = numbers[1:4]
print(extracted_elements)  
#What would be the output of numbers[::-1]
#(5, 4, 3, 2, 1)

#4Create two tuples, fruits with elements 'apple', 'banana', and 
# berries with elements 'strawberry', 'blueberry'.
all_fruits = ('apple', 'banana', 'strawberry', 'blueberry')
fruits = all_fruits[:2]
berries = all_fruits[2:]
#Concatenate the two tuples and store the result in a new tuple named combined_fruits
combined_fruits = fruits + berries
#Repeat the combined_fruits tuple three times and print the result.
repeated_fruits = combined_fruits * 3
print(repeated_fruits)


#5 Create a tuple named grades with the elements 90, 85, 92, 88, 95
grades = (90, 85, 92, 88, 95)
#Use the count() method to find how many times the grade 88 appears in the tuple
frequency_of_88 = grades.count(88)
print(f"The grade 88 appears {frequency_of_88} time(s) in the tuple.")
#Use the index() method to find the index of the grade 92.
index_of_92 = grades.index(92)
print(f"The grade 92 is located at index {index_of_92} in the tuple.")


#6 Create a tuple named mixed_types with elements 'apple', 42, and 3.14
mixed_types = ('apple', 42, 3.14)
#Access and print the second element of the tuple
mixed_types = ('apple', 42, 3.14)
print(mixed_types[1])

'''Question 6
You are managing the inventory for a small bookstore. 
Create a list of book titles available in the store. 
Add new titles to the list as they arrive. If a book is sold out, 
remove it from the list. Write a function to check if a specific book is in stock.
'''
class Bookstore:
    def __init__(self):
        self.inventory = []

    def add_book(self, title):
        self.inventory.append(title)

    def remove_book(self, title):
        if title in self.inventory:
            self.inventory.remove(title)

    def check_availability(self, title):
        return title in self.inventory

    def display_inventory(self):
        print("Current Inventory:")
        for book in self.inventory:
            print(book)


# Create a bookstore
bookstore = Bookstore()

# Add some initial books
bookstore.add_book("To Kill a Mockingbird")
bookstore.add_book("1984")
bookstore.add_book("The Great Gatsby")
bookstore.add_book("Pride and Prejudice")
bookstore.add_book("The Catcher in the Rye")

# Display the initial inventory
bookstore.display_inventory()

# Check if a book is in stock
print("Is '1984' in stock?", bookstore.check_availability("1984"))

# Sell a book
bookstore.remove_book("The Great Gatsby")
print("After selling 'The Great Gatsby':")
bookstore.display_inventory()

# Add new books
bookstore.add_book("The Hunger Games")
bookstore.add_book("Divergent")
print("After adding new books:")
bookstore.display_inventory()

# Check if a book is in stock
print("Is 'Pride and Prejudice' in stock?", bookstore.check_availability("Pride and Prejudice"))

# Sell another book
bookstore.remove_book("Pride and Prejudice")
print("After selling 'Pride and Prejudice':")
bookstore.display_inventory()

'''Question 7
 You have a list of grades for a class of students. 
 Write a function to add a new grade to the list. 
 Another function should remove the lowest grade.
 Write a third function to calculate the average grade.
'''

class GradeBook:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def remove_lowest_grade(self):
        if self.grades:
            self.grades.remove(min(self.grades))

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0


# Create a grade book
grade_book = GradeBook()

# Add some initial grades
grade_book.add_grade(90)
grade_book.add_grade(80)
grade_book.add_grade(70)
grade_book.add_grade(95)

# Display the initial grades
print("Initial Grades:", grade_book.grades)

# Add a new grade
grade_book.add_grade(85)
print("After adding a new grade:", grade_book.grades)

# Remove the lowest grade
grade_book.remove_lowest_grade()
print("After removing the lowest grade:", grade_book.grades)

# Calculate the average grade
print("Average Grade:", grade_book.calculate_average())


'''Question 8
Implement a simple to-do list application. 
Create a list to store tasks. Write functions to add a task, 
remove a task by its name, and display all tasks. Ensure that the 
tasks are displayed in the order they were added.
'''
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")


# Create a to-do list
todo_list = ToDoList()

# Add some initial tasks
todo_list.add_task("Buy groceries")
todo_list.add_task("Do laundry")
todo_list.add_task("Clean the house")

# Display the initial tasks
print("Initial Tasks:")
todo_list.display_tasks()

# Add a new task
todo_list.add_task("Walk the dog")
print("\nAfter adding a new task:")
todo_list.display_tasks()

# Remove a task
todo_list.remove_task("Do laundry")
print("\nAfter removing a task:")
todo_list.display_tasks()

'''Question 9
Create a list to store items you need to buy from the grocery store. 
Write functions to add items, remove items, and check if a specific item is 
already on the list. Ensure that duplicate items are not added.
'''
class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def check_item(self, item):
        return item in self.items

    def display_list(self):
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")


# Create a grocery list
grocery_list = GroceryList()

# Add some initial items
grocery_list.add_item("Milk")
grocery_list.add_item("Bread")
grocery_list.add_item("Eggs")

# Display the initial items
print("Initial Items:")
grocery_list.display_list()

# Add a new item
grocery_list.add_item("Apples")
print("\nAfter adding a new item:")
grocery_list.display_list()

# Try to add a duplicate item
grocery_list.add_item("Milk")
print("\nAfter trying to add a duplicate item:")
grocery_list.display_list()

# Remove an item
grocery_list.remove_item("Bread")
print("\nAfter removing an item:")
grocery_list.display_list()

# Check if an item is on the list
print("\nIs 'Eggs' on the list?", grocery_list.check_item("Eggs"))
print("Is 'Bread' on the list?", grocery_list.check_item("Bread"))


'''Question 10
You are tracking daily temperatures for a month. 
Create a list to store these temperatures. Write functions to 
find the highest and lowest temperatures, and to calculate the 
average temperature for the month.
'''
class TemperatureTracker:
    def __init__(self):
        self.temperatures = []

    def add_temperature(self, temperature):
        self.temperatures.append(temperature)

    def find_highest_temperature(self):
        return max(self.temperatures)

    def find_lowest_temperature(self):
        return min(self.temperatures)

    def calculate_average_temperature(self):
        return sum(self.temperatures) / len(self.temperatures)

    def display_temperatures(self):
        for i, temperature in enumerate(self.temperatures, 1):
            print(f"Day {i}: {temperature}°C")


# Create a temperature tracker
temperature_tracker = TemperatureTracker()

# Add some temperatures
temperature_tracker.add_temperature(22)
temperature_tracker.add_temperature(25)
temperature_tracker.add_temperature(20)
temperature_tracker.add_temperature(28)
temperature_tracker.add_temperature(24)
temperature_tracker.add_temperature(26)
temperature_tracker.add_temperature(21)
temperature_tracker.add_temperature(27)
temperature_tracker.add_temperature(23)
temperature_tracker.add_temperature(29)
temperature_tracker.add_temperature(30)

# Display the temperatures
print("Temperatures:")
temperature_tracker.display_temperatures()

# Find the highest temperature
print("\nHighest Temperature:", temperature_tracker.find_highest_temperature(), "°C")

# Find the lowest temperature
print("Lowest Temperature:", temperature_tracker.find_lowest_temperature(), "°C")

# Calculate the average temperature
print("Average Temperature:", temperature_tracker.calculate_average_temperature(), "°C")


'''Question 11
You are responsible for assigning seats to students in a classroom. 
Create a list to represent the seating arrangement. Write functions to 
assign a seat to a new student, find a student's seat by name, and swap 
seats between two students.
'''
class Classroom:
    def __init__(self, num_seats):
        self.seats = [None] * num_seats

    def assign_seat(self, student, seat_number):
        if self.seats[seat_number - 1] is None:
            self.seats[seat_number - 1] = student
            print(f"Seat {seat_number} assigned to {student}.")
        else:
            print(f"Seat {seat_number} is already occupied.")

    def find_seat(self, student):
        if student in self.seats:
            return self.seats.index(student) + 1
        else:
            return None

    def swap_seats(self, student1, student2):
        seat1 = self.find_seat(student1)
        seat2 = self.find_seat(student2)
        if seat1 and seat2:
            self.seats[seat1 - 1], self.seats[seat2 - 1] = self.seats[seat2 - 1], self.seats[seat1 - 1]
            print(f"Seats of {student1} and {student2} swapped.")
        else:
            print("One or both students are not in the classroom.")

    def display_seats(self):
        for i, student in enumerate(self.seats, 1):
            print(f"Seat {i}: {student}")


# Create a classroom with 10 seats
classroom = Classroom(10)

# Assign seats to students
classroom.assign_seat("Alice", 1)
classroom.assign_seat("Bob", 2)
classroom.assign_seat("Charlie", 3)
classroom.assign_seat("David", 4)
classroom.assign_seat("Eve", 5)

# Display the seats
print("Initial Seating Arrangement:")
classroom.display_seats()

# Find a student's seat
print("\nAlice's seat:", classroom.find_seat("Alice"))

# Swap seats between two students
classroom.swap_seats("Alice", "Bob")

# Display the seats after swapping
print("\nSeating Arrangement after swapping:")
classroom.display_seats()


'''Question 12
You are organizing an event and need to manage the guest list. 
Create a list to store the names of the guests. Write functions to 
add a guest, remove a guest by name, and check if a person is on the guest list.

'''
class GuestList:
    def __init__(self):
        self.guests = []

    def add_guest(self, name):
        if name not in self.guests:
            self.guests.append(name)
            print(f"{name} has been added to the guest list.")
        else:
            print(f"{name} is already on the guest list.")

    def remove_guest(self, name):
        if name in self.guests:
            self.guests.remove(name)
            print(f"{name} has been removed from the guest list.")
        else:
            print(f"{name} is not on the guest list.")

    def is_on_list(self, name):
        if name in self.guests:
            return True
        else:
            return False

    def display_guests(self):
        print("Guest List:")
        for guest in self.guests:
            print(guest)


# Create a guest list
guest_list = GuestList()

# Add guests to the list
guest_list.add_guest("Alice")
guest_list.add_guest("Bob")
guest_list.add_guest("Charlie")
guest_list.add_guest("David")
guest_list.add_guest("Eve")

# Display the guest list
print("Initial Guest List:")
guest_list.display_guests()

# Check if a person is on the guest list
print("\nIs Alice on the guest list?", guest_list.is_on_list("Alice"))

# Remove a guest from the list
guest_list.remove_guest("Bob")

# Display the guest list after removing a guest
print("\nGuest List after removing Bob:")
guest_list.display_guests()


'''Question 13
 Create a playlist for a party. 
 Use a list to store song titles. 
 Write functions to add a song, remove a song by title, 
 and shuffle the playlist. Ensure no duplicate songs are added to the playlist.
'''
import random

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title):
        if title not in self.songs:
            self.songs.append(title)
            print(f"{title} has been added to the playlist.")
        else:
            print(f"{title} is already on the playlist.")

    def remove_song(self, title):
        if title in self.songs:
            self.songs.remove(title)
            print(f"{title} has been removed from the playlist.")
        else:
            print(f"{title} is not on the playlist.")

    def shuffle_playlist(self):
        random.shuffle(self.songs)
        print("Playlist has been shuffled.")

    def display_playlist(self):
        print("Playlist:")
        for i, song in enumerate(self.songs, 1):
            print(f"{i}. {song}")


# Create a playlist
playlist = Playlist()

# Add songs to the playlist
playlist.add_song("Happy")
playlist.add_song("Uptown Funk")
playlist.add_song("Can't Stop the Feeling!")
playlist.add_song("We Found Love")
playlist.add_song("Happy")  # Try to add a duplicate song

# Display the playlist
print("Initial Playlist:")
playlist.display_playlist()

# Remove a song from the playlist
playlist.remove_song("Uptown Funk")

# Display the playlist after removing a song
print("\nPlaylist after removing Uptown Funk:")
playlist.display_playlist()

# Shuffle the playlist
playlist.shuffle_playlist()

# Display the shuffled playlist
print("\nShuffled Playlist:")
playlist.display_playlist()

'''Question 14
You are managing course enrollments for a university. 
Create a list of students enrolled in a course. Write functions 
to add a student, remove a student by name, and find the total number 
of students enrolled.
'''
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} has been added to {self.course_name}.")
        else:
            print(f"{student_name} is already enrolled in {self.course_name}.")

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} has been removed from {self.course_name}.")
        else:
            print(f"{student_name} is not enrolled in {self.course_name}.")

    def get_enrollment(self):
        return len(self.students)

    def display_enrollment(self):
        print(f"Enrollment for {self.course_name}:")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")


# Create a course
course = Course("Introduction to Computer Science")

# Add students to the course
course.add_student("Alice")
course.add_student("Bob")
course.add_student("Charlie")
course.add_student("David")
course.add_student("Alice")  # Try to add a duplicate student

# Display the enrollment
print("Initial Enrollment:")
course.display_enrollment()

# Remove a student from the course
course.remove_student("Bob")

# Display the enrollment after removing a student
print("\nEnrollment after removing Bob:")
course.display_enrollment()

# Get the total number of students enrolled
print(f"\nTotal students enrolled: {course.get_enrollment()}")


'''Question 15
You are creating a recipe management system. 
Create a list of ingredients required for a recipe. 
Write functions to add an ingredient, remove an ingredient by name, 
and check if a specific ingredient is in the list. Sort the list of 
ingredients alphabetically.
'''
class Recipe:
    def __init__(self, recipe_name):
        self.recipe_name = recipe_name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            self.ingredients.sort()
            print(f"{ingredient} has been added to {self.recipe_name}.")
        else:
            print(f"{ingredient} is already in {self.recipe_name}.")

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            print(f"{ingredient} has been removed from {self.recipe_name}.")
        else:
            print(f"{ingredient} is not in {self.recipe_name}.")

    def has_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def display_ingredients(self):
        print(f"Ingredients for {self.recipe_name}:")
        for i, ingredient in enumerate(self.ingredients, 1):
            print(f"{i}. {ingredient}")


# Create a recipe
recipe = Recipe("Chocolate Cake")

# Add ingredients to the recipe
recipe.add_ingredient("Flour")
recipe.add_ingredient("Sugar")
recipe.add_ingredient("Eggs")
recipe.add_ingredient("Cocoa Powder")
recipe.add_ingredient("Flour")  # Try to add a duplicate ingredient

# Display the ingredients
print("Initial Ingredients:")
recipe.display_ingredients()

# Remove an ingredient from the recipe
recipe.remove_ingredient("Eggs")

# Display the ingredients after removing an ingredient
print("\nIngredients after removing Eggs:")
recipe.display_ingredients()

# Check if a specific ingredient is in the recipe
print(f"\nIs Sugar in the recipe? {recipe.has_ingredient('Sugar')}")
print(f"Is Milk in the recipe? {recipe.has_ingredient('Milk')}")
