# PYTHON SETS

'''QUESTION 1
You have two sets representing students enrolled in Math and Science classes. 
Find the set of students who are enrolled in both classes.'''

# Set of students enrolled in Math class
math_students = {"Alice", "Bob", "Charlie", "David", "Emily"}

# Set of students enrolled in Science class
science_students = {"Bob", "Charlie", "Emily", "Frank", "George"}

# Find the set of students who are enrolled in both classes
both_classes = math_students & science_students

print("Students enrolled in both Math and Science classes:", both_classes)


'''QUESTION 2
Given a set of unique employee IDs, add a new employee ID to the set
'''

# Set of unique employee IDs
employee_ids = {101, 102, 103, 104, 105}

# New employee ID to add
new_id = 106

# Add the new employee ID to the set
employee_ids.add(new_id)

print("Updated set of employee IDs:", employee_ids)


'''QUESTION 3
You are managing two different projects and have two sets representing the team members for each project. 
Find the set of team members who are working on either project or both projects.
'''

# Set of team members for Project A
project_a_team = {"John", "Mary", "David", "Emily"}

# Set of team members for Project B
project_b_team = {"Mary", "David", "Kevin", "Sarah"}

# Find the set of team members who are working on either project or both projects
all_team_members = project_a_team.union(project_b_team)

print("Team members working on either project or both projects:", all_team_members)



'''QUESTION 4
You have a set of customer IDs who have made purchases this month. 
Remove a customer ID from the set who has canceled their order
'''

# Set of customer IDs who have made purchases this month
customer_ids = {101, 102, 103, 104, 105}

# Customer ID to remove (who has canceled their order)
canceled_id = 103

# Remove the customer ID from the set
customer_ids.discard(canceled_id)

print("Updated set of customer IDs:", customer_ids)


'''QUESTION 5
Given two sets of product IDs, one representing products in stock and the other 
representing products that have been sold, 
find the set of products that are still in stock.'''

# Set of product IDs in stock
in_stock = {101, 102, 103, 104, 105}

# Set of product IDs that have been sold
sold = {102, 104, 106}

# Find the set of products that are still in stock
still_in_stock = in_stock.difference(sold)

print("Products still in stock:", still_in_stock)


'''QUESTION 6
You have a set of registered conference attendees. 
Check if a particular person is registered
'''

# Set of registered conference attendees
attendees = {"John Doe", "Jane Smith", "Bob Johnson", "Alice Brown"}

# Person to check
person = "Jane Smith"

# Check if the person is registered
if person in attendees:
    print(f"{person} is registered for the conference.")
else:
    print(f"{person} is not registered for the conference.")



'''QUESTION 7
Given two sets of book titles, one representing books available in the library and 
the other representing books borrowed by students, 
find the set of books that are not currently available in the library.'''

# Set of book titles available in the library
library_books = {"Book A", "Book B", "Book C", "Book D", "Book E"}

# Set of book titles borrowed by students
borrowed_books = {"Book B", "Book D", "Book F"}

# Find the set of books that are not currently available in the library
unavailable_books = borrowed_books.difference(library_books)

print("Books not currently available in the library:", unavailable_books)


'''QUESTION 8
You have a set of unique tags assigned to a blog post. 
Add multiple new tags to the set at once.
'''

# Initial set of unique tags assigned to a blog post
tags = {"python", "programming", "development"}

# New tags to add
new_tags = {"machine learning", "artificial intelligence", "data science"}

# Add the new tags to the set
tags.update(new_tags)

print("Updated tags:", tags)


'''QUESTION 9 
Given a set of employee skills and another set of skills required for a new project, 
find the set of skills that need to be acquired or improved.
'''

# Set of employee skills
employee_skills = {"python", "java", "communication", "teamwork"}

# Set of skills required for the new project
project_skills = {"python", "java", "machine learning", "data science", "leadership"}

# Find the set of skills that need to be acquired or improved
skills_to_acquire = project_skills.difference(employee_skills)

print("Skills to acquire or improve:", skills_to_acquire)


'''QUESTION 10 
You have two sets of favorite movies from two different friends. 
Find the set of movies that are favorite to at least one of them but not both.
'''

# Set of favorite movies from friend 1
friend1_movies = {"The Shawshank Redemption", "The Godfather", "The Dark Knight", "12 Angry Men"}

# Set of favorite movies from friend 2
friend2_movies = {"The Godfather", "The Dark Knight", "Inception", "Interstellar"}

# Find the set of movies that are favorite to at least one of them but not both
unique_movies = friend1_movies.symmetric_difference(friend2_movies)

print("Movies favorite to at least one of them but not both:", unique_movies)



'''QUESTION 11
Given a set of emails collected from a signup form, ensure that the set contains only unique emails by 
checking the length before and after adding more emails
'''

# Initial set of emails
emails = {"john@example.com", "jane@example.com", "bob@example.com"}

print("Initial set of emails:", emails)
print("Length of initial set:", len(emails))

# New emails to add
new_emails = {"alice@example.com", "john@example.com", "charlie@example.com"}

# Add new emails to the set
emails.update(new_emails)

print("\nUpdated set of emails:", emails)
print("Length of updated set:", len(emails))

# Check if the length has changed
if len(emails) == len(emails.union(new_emails)):
    print("No duplicates added.")
else:
    print("Duplicates were added.")


'''QUESTION 12
You have a set of courses you are interested in and another set of courses you have completed. 
Find the set of courses you are still interested in but have not yet completed.'''

# Set of courses you are interested in
interested_courses = {"Python", "Java", "Data Science", "Machine Learning", "AI"}

# Set of courses you have completed
completed_courses = {"Python", "Java", "Data Science"}

# Find the set of courses you are still interested in but have not yet completed
remaining_courses = interested_courses.difference(completed_courses)

print("Courses you are still interested in but have not yet completed:", remaining_courses)


'''QUESTION 13
Given a set of cities visited last year and another set of cities visited this year, 
find the set of cities that were visited in either year but not both
'''

cities_last_year = {"New York", "Los Angeles", "Chicago", "Houston"}
cities_this_year = {"New York", "San Francisco", "Miami", "Chicago"}

cities_visited_either_year = cities_last_year.symmetric_difference(cities_this_year)

print("Cities visited in either year but not both:", cities_visited_either_year)


'''QUESTION 14
You have a set of parts required to build a machine. 
Remove a part from the set if it is faulty.
'''

# Set of parts required to build a machine
parts_required = {"Gear", "Motor", "Bearing", "Screw", "Piston"}

# Set of faulty parts
faulty_parts = {"Bearing", "Screw"}

# Remove faulty parts from the set of parts required
parts_required -= faulty_parts

print("Parts required to build a machine (after removing faulty parts):", parts_required)


'''QUESTION 15
Given two sets representing two different sports clubs' members, 
find the set of members who are exclusive to the first club
'''

# Set of members of Club A
club_a_members = {"John", "Mary", "David", "Emily", "Michael"}

# Set of members of Club B
club_b_members = {"Mary", "David", "Sarah", "Tom", "Lily"}

# Find the set of members who are exclusive to Club A
exclusive_to_club_a = club_a_members - club_b_members

print("Members exclusive to Club A:", exclusive_to_club_a)


'''QUESTION 16
You have a set of ingredients required for a recipe.
Check if a specific ingredient is missing.
'''

# Set of ingredients required for the recipe
required_ingredients = {"flour", "sugar", "eggs", "butter", "vanilla"}

# Set of ingredients you have
available_ingredients = {"flour", "sugar", "eggs", "vanilla"}

# Check if a specific ingredient is missing
missing_ingredient = "butter"

if missing_ingredient not in available_ingredients:
    print(f"You are missing {missing_ingredient}!")
else:
    print(f"You have {missing_ingredient}!")


'''QUESTION 17 
Given a set of friends on social media and another set of mutual friends with a colleague, 
find the set of mutual friends.
'''

friends_on_social_media = {"John", "Mary", "David", "Emily", "Michael"}
mutual_friends_with_colleague = {"Mary", "David", "Sarah", "Tom", "Lily"}

mutual_friends = friends_on_social_media & mutual_friends_with_colleague

print("Mutual friends:", mutual_friends)


'''QUESTION 18
You have a set of items in your inventory and another set representing items that need restocking. 
Find the set of items that are currently in stock and need restocking.
'''

items_in_inventory = {"apple", "banana", "orange", "grape", "pear"}
items_needing_restocking = {"apple", "banana", "mango", "pineapple"}

items_to_restock = items_in_inventory & items_needing_restocking

print("Items to restock:", items_to_restock)


'''QUESTION 19
Given a set of languages spoken by employees in a company and another set of languages required for a new project, 
find the set of languages that are both spoken by employees and required for the project.
'''

languages_spoken_by_employees = {"English", "Spanish", "French", "Mandarin", "Arabic"}
languages_required_for_project = {"English", "French", "German", "Italian", "Spanish"}

languages_available_for_project = languages_spoken_by_employees & languages_required_for_project

print("Languages available for the project:", languages_available_for_project)


'''QUESTION 20
You have a set of completed tasks and another set of tasks for a project. 
Find the set of tasks that are yet to be completed.
'''

completed_tasks = {"Task A", "Task B", "Task C", "Task D"}
all_tasks_for_project = {"Task A", "Task B", "Task C", "Task D", "Task E", "Task F", "Task G"}

tasks_yet_to_be_completed = all_tasks_for_project - completed_tasks

print("Tasks yet to be completed:", tasks_yet_to_be_completed)



# DICTIONARIES AND DICTIONARY METHOD

'''QUESTION 1 
You have a dictionary representing the inventory of a store with item names as keys and quantities as values. 
Add a new item to the inventory with a specific quantity
'''

inventory = {"Apple": 10, "Banana": 20, "Orange": 30}

new_item = "Grapes"
new_quantity = 40

inventory[new_item] = new_quantity

print("Updated inventory:", inventory)


'''QUESTION 2
Given a dictionary of student names and their scores, 
find the score of a particular student.
'''

def find_student_score(student_scores, student_name):
    if student_name in student_scores:
        return student_scores[student_name]
    else:
        return "Student not found"

# Example usage:
student_scores = {"John": 85, "Alice": 92, "Bob": 78}
student_name = "Alice"
print(find_student_score(student_scores, student_name))  


'''QUESTION 3 
You have a dictionary of country names as keys and their capitals as values. 
Update the capital of a specific country.
'''

country_capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid"
}

country_to_update = "Germany"
new_capital = "Munich"

if country_to_update in country_capitals:
    country_capitals[country_to_update] = new_capital
    print("Capital updated successfully!")
else:
    print("Country not found in the dictionary.")

print("Updated country capitals:", country_capitals)

'''Question 4
Given a dictionary of product prices with product names as keys, 
remove a product from the dictionary.
'''
def remove_product(prices, product_name):
    if product_name in prices:
        del prices[product_name]
        print(f"{product_name} has been removed from the prices.")
    else:
        print(f"{product_name} is not in the prices.")

# Create a dictionary of product prices
prices = {
    "Apple": 1.00,
    "Banana": 0.50,
    "Cherry": 2.00,
    "Date": 1.50,
    "Elderberry": 3.00
}

# Display the initial prices
print("Initial Prices:")
for product, price in prices.items():
    print(f"{product}: ${price:.2f}")

# Remove a product from the prices
remove_product(prices, "Banana")

# Display the prices after removing a product
print("\nPrices after removing Banana:")
for product, price in prices.items():
    print(f"{product}: ${price:.2f}")

# Try to remove a product that is not in the prices
remove_product(prices, "Fig")


'''Question 5
You have two dictionaries representing two different departments with 
employee names as keys and their salaries as values. 
Merge these two dictionaries into one.
'''
def merge_departments(dept1, dept2):
    merged_dept = {**dept1, **dept2}
    return merged_dept

# Create two dictionaries representing two different departments
dept1 = {
    "John": 50000,
    "Alice": 60000,
    "Bob": 70000
}

dept2 = {
    "Mike": 40000,
    "Emma": 55000,
    "Oliver": 65000
}

# Merge the two departments
merged_dept = merge_departments(dept1, dept2)

# Display the merged department
print("Merged Department:")
for employee, salary in merged_dept.items():
    print(f"{employee}: ${salary}")

'''Question 6
Given a dictionary of city names and their populations, 
check if a particular city is in the dictionary.
'''
def check_city(cities, city_name):
    if city_name in cities:
        print(f"{city_name} is in the dictionary with a population of {cities[city_name]}")
    else:
        print(f"{city_name} is not in the dictionary")

# Create a dictionary of city names and their populations
cities = {
    "New York": 8405837,
    "Los Angeles": 3990456,
    "Chicago": 2695598,
    "Houston": 2320268,
    "Phoenix": 1730375
}

# Check if a particular city is in the dictionary
check_city(cities, "New York")
check_city(cities, "San Francisco")


'''Question 7
You have a dictionary of book titles as keys and their authors as values. 
Add multiple new books to the dictionary at once.
'''
def add_books(books, new_books):
    books.update(new_books)
    return books

# Create a dictionary of book titles and their authors
books = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald"
}

# Add multiple new books to the dictionary at once
new_books = {
    "Pride and Prejudice": "Jane Austen",
    "The Catcher in the Rye": "J.D. Salinger",
    "War and Peace": "Leo Tolstoy"
}

# Add the new books to the dictionary
books = add_books(books, new_books)

# Display the updated dictionary
print("Updated Dictionary:")
for book, author in books.items():
    print(f"{book}: {author}")


'''Question 8 
Given a dictionary of students' names and their grades, 
find the student with the highest grade.
'''
def find_top_student(grades):
    top_student = max(grades, key=grades.get)
    return top_student, grades[top_student]

# Create a dictionary of students' names and their grades
grades = {
    "Alice": 95,
    "Bob": 92,
    "Charlie": 98,
    "David": 90,
    "Eve": 96
}

# Find the student with the highest grade
top_student, top_grade = find_top_student(grades)

print(f"The student with the highest grade is {top_student} with a grade of {top_grade}")


'''Question 9
You have a dictionary representing a phone book with names as keys and phone numbers as values. 
Remove a contact from the phone book.
'''
def remove_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

# Example usage:
phone_book = {
    "Alice": "1234567",
    "Bob": "8901234",
    "Charlie": "5678901"
}

remove_contact(phone_book, "Bob")
print(phone_book)  # Output: {"Alice": "1234567", "Charlie": "5678901"}


'''Question 10
Given a dictionary of countries and their populations, 
create a new dictionary with only those countries that have a 
population greater than a specified number.
'''
def filter_countries(countries, min_population):
    filtered_countries = {country: population for country, population in countries.items() if population > min_population}
    return filtered_countries

# Example usage:
countries = {
    "USA": 331002651,
    "Canada": 37742154,
    "Mexico": 127575529,
    "UK": 67886011,
    "France": 67391582
}

min_population = 50000000
result = filter_countries(countries, min_population)
print(result)  # Output: {"USA": 331002651, "Mexico": 127575529}
