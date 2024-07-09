'''QUESTION 1
You're creating a program to manage a zoo's animal population. 
Declare a variable lion_population with an initial value of 10. 
The zoo welcomes 5 new lion cubs. Update the lion_population variable and 
print the total lion population.
'''

lion_population = 10
# Update the lion population with the new cubs
lion_population += 5
# Print the total lion population
print("The total lion population is:", lion_population)


'''QUESTION 2
You're developing a weather monitoring system. 
Declare a variable temperature with a value of 25.5 degrees Celsius. 
Due to a sudden heatwave, the temperature increases by 8 degrees. 
Update and print the new temperature
'''
temperature = 25.5  # Initial temperature in degrees Celsius
# Update the temperature due to the heatwave
temperature += 8
# Print the new temperature
print("The new temperature is:", temperature, "degrees Celsius")


'''QUESTION 3
A science experiment involves tracking the growth of a plant. 
Declare a variable plant_height with an initial value of 15 centimeters. 
Over a week, the plant grows 2.5 centimeters taller each day. 
Update and print the final height of the plant after the week.
'''

plant_height = 15  # Initial height in centimeters
# Calculate the total growth over the week
total_growth = 2.5 * 7  # 2.5 cm/day * 7 days
# Update the plant height
plant_height += total_growth
# Print the final height of the plant
print("The final height of the plant is:", plant_height, "centimeters")


'''QUESTION 4
You're designing a space mission trajectory. 
Declare variables initial_velocity and acceleration with values 3000 meters per second 
and 500 meters per second squared respectively. Calculate and print the final velocity after 10 seconds
'''

initial_velocity = 3000  # Initial velocity in meters per second
acceleration = 500  # Acceleration in meters per second squared
time = 10  # Time in seconds
# Calculate the final velocity using the equation: v = u + at
final_velocity = initial_velocity + acceleration * time
# Print the final velocity
print("The final velocity after 10 seconds is:", final_velocity, "meters per second")


'''QUESTION 5
A group of friends is sharing a pizza. 
Declare a variable pizza_slices with a value of 8. 
Each friend wants to have an equal number of slices, and there are 5 friends. 
Calculate and print the maximum number of slices each friend can have without cutting the pizza
'''

pizza_slices = 8  # Total number of pizza slices
num_friends = 5  # Number of friends
# Calculate the maximum number of slices each friend can have
slices_per_friend = pizza_slices // num_friends
# Print the result
print("Each friend can have a maximum of", slices_per_friend, "slices without cutting the pizza.")


'''QUESTION 6
You're modeling the movement of a pendulum. Declare a variable pendulum_length with a value of 1.2 meters. 
Calculate and print the period of oscillation
'''
import math
pendulum_length = 1.2  # Length of the pendulum in meters
g = 9.81  # Acceleration due to gravity in meters per second squared
# Calculate the period of oscillation using the formula: T = 2*pi*sqrt(L/g)
period = 2 * math.pi * math.sqrt(pendulum_length / g)
# Print the result
print("The period of oscillation is approximately {:.2f} seconds.".format(period))


'''QUESTION 7
A software company is tracking the number of bugs in their codebase. 
Declare a variable bug_count with an initial value of 100. After a round of debugging, 35 bugs are fixed. 
Update and print the new bug_count
'''

bug_count = 100  # Initial number of bugs
# Fix 35 bugs
bug_count = bug_count - 35
# Print the new bug count
print("The new bug count is:", bug_count)


'''QUESTION 8
You're building a game where players collect gems. 
Declare a variable gem_count with an initial value of 50. 
Each time a player finds a gem, 5 gems are added to their collection. 
Update and print the new gem_count
'''

gem_count = 50  # Initial number of gems
# Player finds a gem, add 5 gems to their collection
gem_count += 5
# Print the new gem count
print("The new gem count is:", gem_count)


'''QUESTION 9
A fitness tracker is monitoring a user's heart rate variability (HRV). 
Declare a variable hrv_index with an initial value of 80. 
After a relaxation session, the user's HRV improves by 10 points. 
Update and print the new hrv_index
'''

hrv_index = 80  # Initial HRV index
# User's HRV improves by 10 points after relaxation session
hrv_index += 10
# Print the new HRV index
print("The new HRV index is:", hrv_index)


'''QUESTION 10
You're simulating the growth of a bacterial colony. 
Declare a variable bacteria_count with an initial value of 5000. 
Over a day, the colony doubles in size every 4 hours. 
Update and print the new bacteria_count
'''

bacteria_count = 5000  # Initial number of bacteria
# Colony doubles in size every 4 hours, so it doubles 6 times in a day (24 hours)
for i in range(6):
    bacteria_count *= 2
# Print the new bacteria count
print("The new bacteria count is:", bacteria_count)