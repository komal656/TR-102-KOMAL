'''Question 1
You have a list of names. Use list comprehension to create a 
new list that contains only the names that start with the letter "A".
'''
names = ["Alice", "Bob", "Adam", "Charlie", "Ava", "Eve"]

# Use list comprehension to create a new list with names starting with "A"
a_names = [name for name in names if name.startswith("A")]

print(a_names)  


'''Question 2
Given a list of temperatures in Fahrenheit, use list comprehension to 
convert each temperature to Celsius and create a new list with these values.
'''
temperatures_f = [32, 75, 90, 50, 25]

# Use list comprehension to convert temperatures to Celsius
temperatures_c = [(temp - 32) * 5/9 for temp in temperatures_f]

print(temperatures_c)  


'''Question 3
You are processing a list of numbers. Use list comprehension to 
create a new list that contains the squares of all the numbers in the original list.
'''
numbers = [1, 2, 3, 4, 5]

# Use list comprehension to create a new list with squares of numbers
squares = [num ** 2 for num in numbers]

print(squares)  


'''Question 4
You have a list of words. Use list comprehension to create a new list that 
contains only the words that have more than 5 characters.
'''
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# Use list comprehension to create a new list with words that have more than 5 characters
long_words = [word for word in words if len(word) > 5]

print(long_words)  


'''Question 5
Given a list of integers, use list comprehension to create a new list containing 
only the even numbers from the original list.
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use list comprehension to create a new list with only the even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)  


'''Question 6
You have a list of prices. Use list comprehension to apply a 10% discount 
to each price and create a new list with the discounted prices.
'''
prices = [10.99, 24.99, 5.99, 19.99, 49.99]

# Use list comprehension to create a new list with discounted prices
discounted_prices = [price * 0.9 for price in prices]

print(discounted_prices)  


'''Question 7
You are working with a list of students' grades. 
Use list comprehension to create a new list that contains the grades that are 
greater than or equal to 60.
'''
grades = [45, 67, 89, 32, 91, 56, 75, 29, 68, 42]

# Use list comprehension to create a new list with grades >= 60
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)  


'''Question 8
Given a list of strings, use list comprehension to create a new list 
where each string is reversed.
'''
strings = ["hello", "world", "python", "programming"]

# Use list comprehension to create a new list with reversed strings
reversed_strings = [string[::-1] for string in strings]

print(reversed_strings)  


'''Question 9 
You have a list of tuples, each containing a product and its price. 
Use list comprehension to create a new list of products that cost more than $20.
'''
products = [("apple", 10.99), ("banana", 0.99), ("orange", 25.99), ("grape", 15.99), ("watermelon", 30.99)]

# Use list comprehension to create a new list of products that cost more than $20
expensive_products = [product for product, price in products if price > 20]

print(expensive_products)  


'''Question 10
You are given a list of mixed data types. Use list comprehension to create a 
new list that contains only the integer values.
'''
mixed_data = [1, "hello", 2.5, 3, "world", 4, None, 5, "python", 6.7]

# Use list comprehension to create a new list that contains only the integer values
integer_values = [value for value in mixed_data if isinstance(value, int)]

print(integer_values)  # Output: [1, 3, 4, 5]


'''DICTIONARY COMPREHENSION'''

'''Question 1
You have a list of student names. Use dictionary comprehension to 
create a dictionary where the keys are the student names and the values are 
the lengths of those names.
'''
student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Use dictionary comprehension to create a dictionary where the keys are the student names and the values are the lengths of those names
name_lengths = {name: len(name) for name in student_names}

print(name_lengths)



'''Question 2
Given a list of numbers, use dictionary comprehension to create a dictionary where 
the keys are the numbers and the values are the squares of those numbers.
'''
numbers = [1, 2, 3, 4, 5]

# Use dictionary comprehension to create a dictionary where the keys are the numbers and the values are the squares of those numbers
squares = {num: num ** 2 for num in numbers}

print(squares)  


'''Question 3
You are given a list of fruits and their prices. 
Use dictionary comprehension to create a dictionary where the keys are the fruits 
and the values are the prices with a 5% tax added.
'''
fruits_and_prices = [("Apple", 1.00), ("Banana", 0.50), ("Cherry", 2.00), ("Date", 1.50), ("Elderberry", 3.00)]

# Use dictionary comprehension to create a dictionary where the keys are the fruits and the values are the prices with a 5% tax added
fruits_with_tax = {fruit: price * 1.05 for fruit, price in fruits_and_prices}

print(fruits_with_tax)  


'''Question 4
You have a list of words. Use dictionary comprehension to create a dictionary where the keys are the words 
and the values are the number of vowels in each word.
'''
words = ["hello", "world", "python", "programming", "dictionary"]

# Use dictionary comprehension to create a dictionary where the keys are the words and the values are the number of vowels in each word
vowels_count = {word: sum(1 for char in word.lower() if char in 'aeiou') for word in words}

print(vowels_count)


'''Question 5
Given a list of employees and their salaries, use dictionary comprehension 
to create a dictionary where the keys are the employee names and the values are their salaries increased by 10%.
'''
employees = [("John", 50000), ("Alice", 60000), ("Bob", 70000), ("Eve", 40000), ("Charlie", 55000)]

# Use dictionary comprehension to create a dictionary where the keys are the employee names and the values are their salaries increased by 10%
salaries_with_raise = {name: salary * 1.1 for name, salary in employees}

print(salaries_with_raise)  