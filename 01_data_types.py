"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
print("------Task 1------")
print()
print()

# Create a float variable
my_float = 9.87

# Convert the float variable to an integer
my_int = int(my_float)

# Print both the original float and the converted integer
print(my_float)
print(my_int)
print("------Task 1------")
print()
print()

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
print("------Task 2------")
print()
print()

# Take input from the user and convert it to a float
number = int(input("Enter an integer: "))

# Check if the number is greater than zero
if number > 0:
    print("Positive")

    # Check if the number is less than zero
elif number < 0:
    print("Negative")

    # If the number is not greater or less than zero, it must be zero
else:
    print("Zero")
print("------Task 2------")
print()
print()

"""
TASK 3:
Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
print("------Task 3------")
print()
print()
# made an input to get a float from an integer
input1 = input("give me a float :")
num1 = float(input1)
#print the float
print(type(num1))



print("------Task 3------")
print()
print()

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
print("------Task 4------")
print()
print()
#made a dictionary
fruit_quantities = dict(
    mangos=10,
    banana=5,
    orange=8,
    grape=15
)

# Printing the quantity of one of the fruits (e.g., orange)
print("Quantity of oranges:", fruit_quantities["orange"])


print("------Task 4------")
print()
print()

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
print("------Task 5------")
print()
print()
#created a string variable
# Create a list of numbers
number_list = [1, 2, 3, 4, 5]

# Convert the list to a string using str()
number_string = str(number_list)[1:-1]  # Removes square brackets

# Convert the string to a tuple of integers using tuple()
number_tuple = tuple(int(num.strip()) for num in number_string.split(','))

# Print both
print("Original string:", number_string)
print("Converted tuple:", number_tuple)


print("------Task 5------")
print()
print()

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
print("------Task 6------")
print()
print()


# Creating a list of favorite subjects
favorite_subjects = ["Math", "science", "English", "History"]

# Joining subjects with a comma separator
comma_separated = ", ".join(favorite_subjects)

# Joining subjects with a " - " separator
dash_separated = " - ".join(favorite_subjects)

# Printing the original list and the joined strings
print("Original list:", favorite_subjects)
print("Comma-separated:", comma_separated)
print("Dash-separated:", dash_separated)
print("------Task 6------")
print()
print()
