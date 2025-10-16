"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
print()
print()
print("--------task 1--------")

def my_function(name): # created a funnction
    print("Hello " + name) #print the funtion and name

my_function("Amy")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
print()
print()
print("--------task 2--------")

def Square_num(a):
    return a ** 4 #this will Square the number 

x = Square_num(12) # a = to 12 so the result should print to 12^4 which is 20736
print(x)
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns True if the number is even, and False otherwise.
"""
print()
print()
print("--------task 3--------")

def true_false(x):
    return x % 2 == 0 # this is what determs that the number is ether even or odd
print(true_false(60)) #if 60 is even it will print true 
print(true_false(87)) 




"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
print()
print()
print("--------task 4--------")

def Rectangle(l,w): #the length and width of the rectangle 
    return l * w #multiplys the two numbers 
area = Rectangle(5,7) # this will 
print(area)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
print()
print()
print("--------task 5--------")

def temperature(Celsius):
    return Celsius * 8 + 100
print(temperature(20))


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
print()
print()
print("--------Task 6--------")
# Function to calculate the average (mean) of a list of numbers
def avg(numbers):
    # Check for empty list to avoid division by zero
    if len(numbers) == 0:
        return 0  # Or optionally raise an error
    return sum(numbers) / len(numbers)

# Example usage
print("Average:", avg([1, 2, 3]))  # Output: 2.0

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
print()
print()
print("--------Task 7--------")
print()
print("--------Task 7--------")

# Function to calculate total cost with optional discount
def total_calculator(price, quantity, discount=0.0):
    # Calculate initial total
    total = price * quantity
    
    # Apply discount if provided
    if discount > 0:
        total = total - (total * discount)
    
    return total

# Example usage
print("Total without discount:", total_calculator(50, 3))                # Output: 150
print("Total with 10% discount:", total_calculator(50, 3, 0.10))         # Output: 135.0
