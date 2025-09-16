'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
print("------Task 1-------")
print()
print()
# greater than 10.
if 11 >= 10:
    print(True)
else:
    print(False)

print("------Task 1-------")
print()
print()

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
print("------Task 2-------")
print()
print()
# Ask if the user is a student
student = input("Are you a student? (yes/no): ").strip().lower()

# Ask for the user's age
age_input = input("What is your age?: ")
age = int(age_input)

# Check student status
is_student = student == "yes"

# Use comparison operators to determine price
if age < 18 or is_student == True:
    price = 10
else:
    price = 20

# Print the ticket price
print("Your ticket price is $" + str(price) + ".")
print("------Task 2-------")
print()
print()
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
print("------Task 3-------")
print()
print()
# List of fruits
fruits = ["apple", "banana", "orange", "grape", "mango"]

# Ask user to enter a fruit name
user_input = input("Enter the name of a fruit: ").strip().lower()

# Check if the fruit is in the list using 'in'
if user_input in fruits:
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.")

print("------Task 3-------")
print()
print()
'''
Exercise 4: x
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''