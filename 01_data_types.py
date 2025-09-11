"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""

# Create a float variable
my_float = 9.87

# Convert the float variable to an integer
my_int = int(my_float)

# Print both the original float and the converted integer
print(my_float)
print(my_int)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
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

"""
TASK 3:
Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
 

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
# wrote subjects down
subjects = "history, english, science, math" 

my_string = "|".join( subjects )


print(my_list) 