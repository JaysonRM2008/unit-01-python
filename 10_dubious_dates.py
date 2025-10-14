from datetime import date
from datetime import time
from datetime import datetime


"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
print("------Exercise 1-------")
print()
print()
# Get the current date and time
current_datetime = datetime.now()

# Print the current date and time
print("Current date and time:", current_datetime)
print("------Exercise 1-------")
print()
print()
"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print("------Exercise 2-------")
print()
print()
# Get the current date
my_date = date.today()

# Format the date as a string in the format MM/DD/YYYY
my_string = my_date.strftime("%m/%d/%Y")

# Get the current date and time
my_dt = datetime.now()

# Print the current date and time object
print(my_dt)

# Print the formatted date string
print(my_string)


print("------Exercise 2-------")
print()
print()
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("------Exercise 3-------")
print()
print()
 #Define the two date strings
date_string1 = "Jan 1 2020"
date_string2 = "Oct 14 2025"

# Define the format string that matches the date strings
date_format = "%b %d %Y"

# Convert the strings to datetime objects using strptime()
date_object1 = datetime.strptime(date_string1, date_format)
date_object2 = datetime.strptime(date_string2, date_format)

# Calculate the difference between the two dates
# This results in a timedelta object
difference = date_object2 - date_object1

# Print the difference in days
print(f"The difference in days is: {difference.days}")
print("------Exercise 3-------")
print()
print()
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print("------Exercise 4-------")
print()
print()
birth_str = input("When is your birthday (YYYY-MM-DD):")
try:
    birth = datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Use YYYY-MM-DD.")
print("------Exercise 4-------")
print()
print()