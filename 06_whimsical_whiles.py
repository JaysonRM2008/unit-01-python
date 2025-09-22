"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
print("------Task 1-------")
print()
print()
# Initialize a counter variable
i = 1

# Use a while loop to print numbers  10
while i <= 10:
    print(i)
    i += 1

print("------Task 1-------")
print()
print()
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print("------Task 2-------")
print()
print()
# Initialize a counter variable
i = 10
while i >= 1:
    print(i)
    i -= 1  #decreasting number

print("------Task 2-------")
print()
print()
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
print("------Task 3-------")
print()
print()
 # Ask the user for a number and convert it to
number = int(input("give me a number: ")) 
result = 1


while number > 0:
    result = number * result
    number -= 1  # Decrease the number by 1 each time
# Print the final result (factorial of the input number)
print(result)

print("------Task 3-------")
print()
print()
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
print("------Task 4-------")
print()
print()
# Predefined password
correct_password = "STEAM"
attempts = 3

while attempts > 0:
    guess = input("Guess the password: ")
    if guess == correct_password:
        print("Access granted! You've guessed the correct password.")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempt(s) left.")
else:
    print("Access denied. You've used all your attempts.")

print("------Task 4-------")
print()
print()
"""
5. Sum of Digits: XX
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
print("------Task 6-------")
print()
print()
n = int(input("How many Fibonacci numbers? "))
a, b, count = 0, 1, 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1

print("------Task 6-------")
print()
print()