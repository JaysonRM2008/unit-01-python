"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
print("------Task 1------")
print()
print()
# Set the correct password
correct_password = "Jayson2001"

# Ask the user to enter a password
entered_password = input("Enter your password: ")

# Check password (case-insensitive)
if entered_password.lower() == correct_password.lower():
    print("Access granted.")
else:
    print("Access denied.")


print("------Task 1------")
print()
print()
"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
print("------Task 2------")
print()
print()
# Ask the user for input
user_input = input("Enter something: ")

# Check if the input is empty
if user_input.strip() == "":
    print("invalid")
else:
    print("valid")
print("------Task 2------")
print()
print()
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
print("------Task 3------")
print()
print()
text = "I saw a Cat, a cAt, a CAT, and a cat in the catalog."

# Replace various capitalizations of "cat"
text = text.replace("cat", "dog")
text = text.replace("Cat", "Dog")
text = text.replace("CAT", "DOG")
text = text.replace("cAt", "dOg")
text = text.replace("caT", "doG")
text = text.replace("cAT", "dOG")
text = text.replace("CaT", "DoG")
text = text.replace("CAt", "DOg")

print(text)

print("------Task 3-------")
print()
print()
"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
print("------Task 4-------")
print()
print()
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Print the result
print("Name:", name)
print("Age:", age)

print("------Task 4-------")
print()
print()

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
print("------Task 5-------")
print()
print()

# Get two float inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prevent division by zero
if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    # Calculate the quotient
    quotient = num1 / num2

    # Round to the nearest tenth
    rounded_result = round(quotient, 1)

    # Print the result
    print("Quotient (rounded to the nearest tenth):", rounded_result)

print("------Task 5-------")
print()
print()
