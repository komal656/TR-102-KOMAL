#Question 1 
age = int(input("Enter your age : "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a  minor.")

#Question 2
print("In degree celcius")
Temperature = int(input("Input the current temperature : "))
if Temperature < 0 :
    print("It's freezing ...")
else:
    print("It's not freeezing ...")

#Question  3
score = int(input("Enter the scores : "))
if score > 90:
    print("Grade A")
if score <= 90 and score >= 80:
    print("Grade B")
else :
    print("Grade C")

#Question 4 
a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))
if a == b:
    print("a and b are equal.")
else:
    print("a and b are not equal.")
    
#Question 5
number = int(input("Enter a number : "))
if number % 2==0:
    print("Even number")
else:
    print("Odd number")

#Question 6
day=int(input("enter the day :"))
if day == 6 & 7 :
    print("weekend")
if day > 7:
    print("Provide a valid day number")
else:
    print("weekday")   


#Question 7 
marks=int(input("Enter your marks : "))
if marks >= 75:
    print("Distinction")
elif marks >= 50 and marks <= 75:
    print("Pass")
else :
    print("Fail")

#Question 8 
speed = int(input("enter the speed"))
if speed >= 120 :
    print("Over speed limit")
else:
    print("Within speed limit")


#Question 9
year = int(input("Enter a year : "))
if year % 4 == 0:
    print("Leap year")
else :
    print("Not a Leap year")

#Question 10
character = input("Enter a variable : ")
if character.lower() in 'a, e, i, o, u':
    print("vowel")
else:
    print("consonant")

#Question 11
x = int(input("enter a Value of x:"))
y = int(input("enter a Value of y:"))
if x > 0 and y > 0:
    print("Both are positive")
else :
    print("At least one is not positive")

#Question 12
time = int(input("enter the time as number (0.00 - 23.59)"))
if time >= 6.00 and time <= 12.00 :
    print("GOOD MORNING")
elif time >= 12.00 and time <= 18.00:
    print("GOOD AFTERNOON")
elif time >= 18.00 and time <= 23.59:
    print("GOOD EVENING")

#Question 13 
budget = int(input("Enter budget : "))
price = int(input("Enter price : "))
if budget >= price :
    print("Purchase possible")
else:
    print("Not enough budget")

#Question 14 
username = input("enter a username for your account")
if username :
    print("username is valid")
else:
    print("username cannot be empty")

#Question 15
weight = input("Enter your weight")
height = input("Enter your height")
BMI = weight / height * height
if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight")
elif BMI >= 25 :
    print("Overweight")

