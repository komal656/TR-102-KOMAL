"""RANDOM MODULE"""
'''1.Create a function that generates a random password of a 
specified length. The password should include uppercase letters, 
lowercase letters, digits, and special characters.
'''
import random
import string

def generate_password(length):
    """
    Generates a random password of a specified length.

    Args:
        length (int): The length of the password to generate.

    Returns:
        str: A random password of the specified length.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    for _ in range(length - 4):
        password.append(random.choice(uppercase_letters + lowercase_letters + digits + special_characters))

    random.shuffle(password)

    return ''.join(password)

# Example usage:
print(generate_password(12))


'''2.Write a function that simulates rolling a pair of six-sided 
dice 100 times. Count how many times the sum of the two dice is equal to 7. 
'''
import random

def roll_dice():
    """
    Simulates rolling a pair of six-sided dice 100 times and counts how many times the sum is equal to 7.

    Returns:
        int: The number of times the sum of the two dice is equal to 7.
    """
    count = 0
    for _ in range(100):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            count += 1
    return count

# Example usage:
print("The sum of the two dice is equal to 7 in", roll_dice(), "out of 100 rolls.")


'''3.Create a program that picks 6 unique random numbers from 1 to 49, 
simulating a lottery draw. 
'''
import random

def lottery_draw():
    """
    Simulates a lottery draw by picking 6 unique random numbers from 1 to 49.

    Returns:
        list: A list of 6 unique random numbers from 1 to 49.
    """
    numbers = random.sample(range(1, 50), 6)
    return numbers

# Example usage:
print("The winning lottery numbers are:", lottery_draw())

'''4.Write a program that randomly selects and displays a quote from a predefined 
list of quotes each time it is run. '''
import random

# Predefined list of quotes
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do something today that your future self will thank you for. - Unknown"
]

def display_quote():
    """
    Randomly selects and displays a quote from the predefined list of quotes.
    """
    quote = random.choice(quotes)
    print("Quote of the day:")
    print(quote)

# Run the program
display_quote()

'''
5.Create a program that randomly selects a movie from a list of movies for a movie night. 
Include functionality to randomly select a genre first and then a movie from that genre. 
'''
import random

# Predefined list of movies, organized by genre
movies = {
    "Action": [
        "Die Hard",
        "The Matrix",
        "Mad Max: Fury Road",
        "The Dark Knight",
        "Indiana Jones and the Raiders of the Lost Ark"
    ],
    "Comedy": [
        "The Hangover",
        "Monty Python and the Holy Grail",
        "The 40-Year-Old Virgin",
        "Anchorman: The Legend of Ron Burgundy",
        "Groundhog Day"
    ],
    "Drama": [
        "The Shawshank Redemption",
        "The Godfather",
        "12 Angry Men",
        "Schindler's List",
        "The Social Network"
    ],
    "Horror": [
        "The Shining",
        "The Exorcist",
        "The Conjuring",
        "Halloween",
        "A Quiet Place"
    ],
    "Romance": [
        "Titanic",
        "Casablanca",
        "When Harry Met Sally",
        "The Notebook",
        "La La Land"
    ]
}

def select_movie():
    """
    Randomly selects a genre and then a movie from that genre for a movie night.
    """
    # Randomly select a genre
    genre = random.choice(list(movies.keys()))
    print(f"Genre for tonight: {genre}")

    # Randomly select a movie from the chosen genre
    movie = random.choice(movies[genre])
    print(f"Movie for tonight: {movie}")

# Run the program
select_movie()

'''6.Write a function that simulates tossing a coin 1000 times. 
Calculate the percentage of heads and tails.
'''
import random

def coin_toss_simulation():
    """
    Simulates tossing a coin 1000 times and calculates the percentage of heads and tails.
    """
    heads = 0
    tails = 0

    for _ in range(1000):
        # Simulate a coin toss (0 = heads, 1 = tails)
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1

    # Calculate the percentage of heads and tails
    heads_percentage = (heads / 1000) * 100
    tails_percentage = (tails / 1000) * 100

    print("Coin Toss Simulation Results:")
    print(f"Heads: {heads} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails} ({tails_percentage:.2f}%)")

# Run the simulation
coin_toss_simulation()


'''DATETIME MODULE'''
'''1. *Event Reminder Application*
   - Your task is to create an event reminder application. 
   The application should accept the event name and event date (in YYYY-MM-DD format) 
   from the user and calculate how many days are left until the event.
'''
from datetime import datetime

def event_reminder():
    """
    Event Reminder Application
    """
    print("Event Reminder Application")

    # Get event name and date from user
    event_name = input("Enter event name: ")
    event_date_str = input("Enter event date (YYYY-MM-DD): ")

    # Parse event date
    event_date = datetime.strptime(event_date_str, "%Y-%m-%d")

    # Calculate days until event
    today = datetime.today()
    days_until_event = (event_date - today).days

    # Print reminder
    if days_until_event < 0:
        print(f"Event '{event_name}' has already passed.")
    elif days_until_event == 0:
        print(f"Event '{event_name}' is today!")
    else:
        print(f"Event '{event_name}' is in {days_until_event} days.")

# Run the application
event_reminder()


'''2. *Time Duration Calculation*
   - Write a program that asks the user to input two times 
   (start time and end time) in HH:MM:SS format. Calculate and print the duration 
   between these two times in hours, minutes, and seconds.
'''
from datetime import datetime

def time_duration_calculation():
    """
    Time Duration Calculation
    """
    print("Time Duration Calculation")

    # Get start and end times from user
    start_time_str = input("Enter start time (HH:MM:SS): ")
    end_time_str = input("Enter end time (HH:MM:SS): ")

    # Parse start and end times
    start_time = datetime.strptime(start_time_str, "%H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%H:%M:%S")

    # Calculate duration
    duration = end_time - start_time

    # Format duration as hours, minutes, and seconds
    hours = duration.seconds // 3600
    minutes = (duration.seconds // 60) % 60
    seconds = duration.seconds % 60

    # Print duration
    print(f"Duration: {hours:02d}:{minutes:02d}:{seconds:02d}")

# Run the application
time_duration_calculation()


'''3. *Date of Birth and Age Calculation*
   - Create a program that asks the user for their date of birth in YYYY-MM-DD 
   format and calculates their current age in years, months, and days.
'''
from datetime import datetime

def calculate_age():
    """
    Date of Birth and Age Calculation
    """
    print("Date of Birth and Age Calculation")

    # Get date of birth from user
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

    # Parse date of birth
    dob = datetime.strptime(dob_str, "%Y-%m-%d")

    # Calculate current age
    today = datetime.today()
    age = today - dob

    # Calculate years, months, and days
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30

    # Print age
    print(f"Your age is {years} years, {months} months, and {days} days.")

# Run the application
calculate_age()


'''MATH MODULES'''
'''1. Write a program that asks the user to input the radius of a circle. 
Calculate and print the area and circumference of the circle using the value of π from the math module.
'''
import math

def calculate_circle_properties():
    """
    Calculate Circle Properties
    """
    print("Calculate Circle Properties")

    # Get radius from user
    radius = float(input("Enter the radius of the circle: "))

    # Calculate area
    area = math.pi * (radius ** 2)

    # Calculate circumference
    circumference = 2 * math.pi * radius

    # Print results
    print(f"Area: {area:.2f} square units")
    print(f"Circumference: {circumference:.2f} units")

# Run the application
calculate_circle_properties()


'''
2. Create a program that accepts the lengths of the two shorter sides of a right triangle. 
Calculate and print the length of the hypotenuse using the Pythagorean theorem'''
import math

def calculate_hypotenuse():
    """
    Calculate Hypotenuse of a Right Triangle
    """
    print("Calculate Hypotenuse of a Right Triangle")

    # Get lengths of shorter sides from user
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))

    # Calculate length of hypotenuse using Pythagorean theorem
    c = math.sqrt(a ** 2 + b ** 2)

    # Print result
    print(f"The length of the hypotenuse is: {c:.2f} units")

# Run the application
calculate_hypotenuse()


'''3. Develop a program to calculate compound interest. 
Ask the user for the principal amount, the annual interest rate, the number of 
times interest is compounded per year, and the number of years. 
Use the math module to perform the calculations.
'''
import math

def calculate_compound_interest():
    """
    Calculate Compound Interest
    """
    print("Calculate Compound Interest")

    # Get user input
    principal = float(input("Enter the principal amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    num_times_compounded_per_year = int(input("Enter the number of times interest is compounded per year: "))
    num_years = int(input("Enter the number of years: "))

    # Convert annual interest rate from percentage to decimal
    annual_interest_rate_decimal = annual_interest_rate / 100

    # Calculate compound interest
    amount = principal * (1 + (annual_interest_rate_decimal / num_times_compounded_per_year)) ** (num_times_compounded_per_year * num_years)

    # Print result
    print(f"The amount after {num_years} years is: ${amount:.2f}")

# Run the application
calculate_compound_interest()