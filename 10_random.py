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
# Roll the dice 
for i in range(1, 11):
     roll_result = random.randint(1, 6)
print(f"Roll {i}: {roll_result}") #prints and rolls dice

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
print(random.choice(my_list)) #print random color

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
#shuffle the list
random.shuffle(my_list)
print(my_list)
print("------Task 4-------")
print()
print()