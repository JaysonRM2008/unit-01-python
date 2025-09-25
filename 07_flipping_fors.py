"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print("------Exercise 1-------")
print()
print()

# Define the string
my_string = "Hello, World!"

for char in my_string:
    # Print the character
    print(char)
print("------Exercise 1-------")
print()
print()

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print("------Exercise 2-------")
print()
print()
# List of numbers
numbers = [10, 20, 30, 40, 50]

# Variable to store the sum
total = 0

# Loop through each number in the list and add to total
for num in numbers:
    total += num

# Print the result
print("The sum of the elements is:", total)

print("------Exercise 2-------")
print()
print()

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print("------Exercise 3-------")
print()
print()
# Input sentence
sentence = "Write a program to print the length of each word"

# Split sentence into words
words = sentence.split()

# Create a list to store lengths
word_lengths = []

# Loop through each word and calculate its length
for word in words:
    word_lengths.append(len(word))

# Print the list of word lengths
print("Word lengths:", word_lengths)

print("------Exercise 3-------")
print()
print()

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print("------Exercise 4-------")
print()
print()
# Create a dictionary with at least 4 key-value pairs
my_dictionary = {
    "name": "Mary",
    "age": 25,
    "city": "New York",
    "occupation": "CEO"
}

# Iterate through the dictionary and print each key-value pair
print("Iterating through the dictionary:")
for key, value in my_dictionary.items():
    print(f"{key}: {value}")
print("------Exercise 4-------")
print()
print()