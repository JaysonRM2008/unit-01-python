text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":  # space character
        count += 1

print(count)
print("------Code 2-------")
print()
print()

print("------Code 3-------")
print()
print()
print("give me a number")
n = input()
print("give me a number")
n_str = input()

# Convert the string input to an integer
n = int(n_str)

for num in range(1, n + 1):  # Correctly loop up to and including the user's number
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")


print("------Code 3-------")
print()
print()

print("------Code 4-------")
print()
print()
num = int(input("Enter an integer: "))

if num < 0:
  print("Factorial does not exist for negative numbers.")
elif num == 0:
  print("The factorial of 0 is 1.")
else:
  result = 1
  for i in range(1, num + 1):  # Correctly includes num in the loop
    result *= i
  print("Factorial of " + str(num) + " is " + str(result)) # Converts integers to strings for printing

  print("------Code 4-------")
print()
print()

print("------Code 5-------")
print()
print()
attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:
        print("Correct password!")
        break  # End the loop if the password is correct
    else:
        print("Incorrect password")
    
    if attempts >= 3:
        print("Too many attempts")
        break  # End the loop after a maximum number of attempts

print("------Code 5-------")
print()
print()

