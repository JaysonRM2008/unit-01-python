"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print("------Exercise 1-------")
print()
print()
for i in range(1, 11):
    print(i)

print("------Exercise 1-------")
print()
print()
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print("------Exercise 2-------")
print()
print()
for x in range (900, 1001, 10):
    print(x)
print("------Exercise 2-------")
print()
print()
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print("------Exercise 3-------")
print()
print()
for x in range (1, 101, 9 ):
    print(x)
print("------Exercise 3-------")
print()
print()
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
print("------Exercise 4-------")
print()
print()
# Initialize a variable to store the sum
total_sum = 0

# Loop through numbers from 1 to 10 (inclusive)
for number in range(1, 11):
    # Add each number to the total_sum
    total_sum += number

# Print the final sum
print(f"The sum of numbers from 1 to 10 is: {total_sum}")
print("------Exercise 4-------")
print()
print()
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
print("------Exercise 5-------")
print()
print()
rows = 5

for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()
     #A triangle of stars, with each row containing one more star than the last.
     # Nested loops, where the outer loop controls the number of rows, and the inner loop prints increasing numbers of stars in each row.
print("------Exercise 5-------")
print()
print()