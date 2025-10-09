import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
print("------Task 1-------")
print()
print()


print("Simulating 10 die rolls:")

# Roll the die 10 times
for i in range(1, 11):
    roll_result = random.randint(1, 6)
    print(f"Roll {i}: {roll_result}")


print("------Task 1-------")
print()
print()
"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print("------Task 2-------")
print()
print()
# Generate 5 random floating-point numbers between 0 and 1
print("Random numbers between 0 and 1:")
i

for _ in range(5):
    roll = random.uniform(0,1)
    print(f"roll: {roll}")
    print()
for _ in range(5):
    roll = random.uniform(10, 20)
    print(f"roll: {roll}")


print("------Task 2-------")
print()
print()
"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print("------Task 3-------")
print()
print()
#make list
my_list = ["red", "blue", "green", "yellow", "purple"]
# Randomly select 3 colors without replacement
selected_colors = random.sample(my_list, 3)

# Print the selected colors
print("Selected colors:", selected_colors)
print("------Task 3-------")
print()
print()
"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print("------Task 4-------")
print()
print()
#make list 1-10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("OG list:")
print(my_list)
#shuffle the list
print("\nshuffle list:")

random.shuffle(my_list)
print(my_list)
print("------Task 4-------")
print()
print()