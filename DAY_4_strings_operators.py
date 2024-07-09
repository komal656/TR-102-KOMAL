#HOW TO USE STRING IN PYTHON (example)
EXAMPLE_string = "HELLO WORLD"
print(EXAMPLE_string)
print(type(EXAMPLE_string))
Example_string = " is a primary code"
print(EXAMPLE_string + Example_string)
print(type(EXAMPLE_string + Example_string))

#String formatted string example
F_name='lal'
M_name=' singh'
L_name=' chadha'
Fu_name = F_name + M_name + L_name
print(Fu_name)

# ... PRACTICAL QUESTIONS ...
# String manipulation
def reverse_string(s):
    return s[::-1]

    # Test the function
input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Original string: {input_string}, Reversed string: {reversed_string}")


# String counting
def count_vowels(s):
    """
    Counts the number of vowels in a given string
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Test the function
input_string = "Hello World"
vowel_count = count_vowels(input_string)
print(f"String: {input_string}, Vowel count: {vowel_count}")


# String Formatting
name = "Rohan"
age = "21"
occupation = "student"
formatted_string = f"My name is {name}, I am {age} years old, and i am a {occupation}."
print(formatted_string)


'''QUESTION 1
You have two variables, a and b, containing integer values. 
Use arithmetic operators to calculate and print the sum, difference, 
product, and quotient of these variables.
'''
a = 10
b = 3

# Calculate and print the sum
sum = a + b
print("Sum:", sum)

# Calculate and print the difference
difference = a - b
print("Difference:", difference)

# Calculate and print the product
product = a * b
print("Product:", product)

# Calculate and print the quotient
if b != 0:
    quotient = a / b
    print("Quotient:", quotient)
else:
    print("Cannot divide by zero!")



'''Question 2
Given a variable x containing an integer value, 
use the modulus operator to check if x is even or odd.
'''
x = 17  # example value

if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")


'''Question 3
You have two variables, a and b. Use comparison operators to check 
if a is greater than b, and print the result.
'''
a = 5
b = 3

if a > b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{a} is not greater than {b}.")


'''Question 4
Given two boolean variables, p and q, use logical operators to 
evaluate and print the result of p AND q, p OR q, and NOT p.
'''
p = True
q = False

# Evaluate and print p AND q
result_and = p and q
print(f"p AND q: {result_and}")

# Evaluate and print p OR q
result_or = p or q
print(f"p OR q: {result_or}")

# Evaluate and print NOT p
result_not = not p
print(f"NOT p: {result_not}")



'''Question 5
You have a variable n containing an integer value. 
Use the bitwise AND, OR, and XOR operators to perform operations with another integer m.
'''
n = 12  # 1100 in binary
m = 10  # 1010 in binary

# Bitwise AND (&)
result_and = n & m
print(f"Bitwise AND (n & m): {result_and} ({bin(result_and)})")

# Bitwise OR (|)
result_or = n | m
print(f"Bitwise OR (n | m): {result_or} ({bin(result_or)})")

# Bitwise XOR (^)
result_xor = n ^ m
print(f"Bitwise XOR (n ^ m): {result_xor} ({bin(result_xor)})")


'''Question 6
Given a variable y containing a floating-point number, 
use the floor division operator to divide y by 2 and print the result.
'''
y = 17.5

# Floor division (//)
result = y // 2
print(f"Floor division (y // 2): {result}")


'''Question 7 
You have two strings, str1 and str2. Use the concatenation operator to 
join these strings and print the result.
'''
str1 = "Hello"
str2 = "World"

# Concatenation using the + operator
result = str1 + str2
print(f"Concatenated string: {result}")
result = "{} {}".format(str1, str2)
print(f"Concatenated string: {result}")

# or using f-strings
result = f"{str1} {str2}"
print(f"Concatenated string: {result}")


'''Question 8
Given a variable z containing an integer, use the increment operator to 
increase its value by 1 and print the result.
'''
z = 5

# Increment z by 1
z += 1

print(f"Incremented value: {z}")
z = 5
print(f"Initial value: {z}")

z += 1
print(f"Incremented value: {z}")

'''Question 9
You have a list my_list and a value val. Use the in operator to check if 
val is present in my_list and print the result.
'''
my_list = [1, 2, 3, 4, 5]
val = 3

# Check if val is in my_list
if val in my_list:
    print(f"{val} is present in my_list")
else:
    print(f"{val} is not present in my_list")


'''Question 10
Given two variables a and b, use the assignment operator to 
assign the value of b to a and print a.
'''
a = 0
b = 10

# Assign the value of b to a
a = b

print(f"The value of a is: {a}")
b = 10
a = b
print(f"The value of a is: {a}")