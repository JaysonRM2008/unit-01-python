"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
print("------Task 1-------")
print()
print()

# Create a list with 4 elements
my_list = ["fire", "leo", "summer", "flames" ]

# Print the list
print("My list:", my_list)
print("------Task 1-------")
print()
print()

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
print("------Task 2-------")
print()
print()

# og list with 4 elements
my_list = ["fire", "leo", "summer", "flames" ]
# Add a new element to the end 
my_list.append("fuego")
# Print the updated list
print("Updated list:", my_list)
print("------Task 2-------")
print()
print()

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
print("------Task 3-------")
print()
print()

# Task 3: Remove Element from a List
my_list = ["fire", "leo", "summer", "flames"]

# Remove the element "flames" from the list
my_list.remove("flames")

# Print the updated list
print("Updated list:", my_list)
print("------Task 3-------")
print()
print()

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
print("------Task 4-------")
print()
print()
# Original list
my_list = ["fire", "leo", "summer", "flames"]

# Modify the element at index 2 (changing "summer" to "autumn")
my_list[2] = "autumn"

# Print the updated list
print("Updated list:", my_list)

print("------Task 4-------")
print()
print()

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
print("------Task 5-------")
print()
print()
# Original list
my_list = ["fire", "leo", "autumn", "flames"]

# Append multiple elements to the list
my_list.extend(["fuego", "ember", "heat"])

# Print the updated list
print("Updated list:", my_list)

print("------Task 5-------")
print()
print()

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
print("------Task 6-------")
print()
print()
# Original list
my_list = ["fire", "leo", "autumn", "flames"]

# Append multiple elements to the list
my_list.extend(["fuego", "ember", "heat"])

# Delete an element at a specific index (for example, index 2)
del my_list[2]

# Print the updated list
print("Updated list after deleting index 2:", my_list)

print("------Task 6-------")
print()
print()

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
print("------Task 7-------")
print()
print()
# Original list
my_list = ["fire", "leo", "autumn", "flames"]
my_list.extend(["fuego", "ember", "heat"])

# Delete an element at a specific index (e.g., index 2)
del my_list[2]  # removes "autumn"

# Task 7: Create a new variable equal to the first 2 items of the list
first_two_items = my_list[:2]

# Print out the new variable
print("First two items:", first_two_items)

print("------Task 7-------")
print()
print()


"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
print("------Task 8-------")
print()
print()
# Original list
my_list = ["fire", "leo", "autumn", "flames"]
my_list.extend(["fuego", "ember", "heat"])

# Delete an element at a specific index (e.g., index 2)
del my_list[2]  # removes "autumn"

# Task 7: Slicing (optional, but we keep the variable)
first_two_items = my_list[:2]

# Task 8: Extend the list with another list
new_elements = ["sun", "lava", "inferno"]
my_list.extend(new_elements)

# Print the updated list
print("Updated list after extension:", my_list)

print("------Task 8-------")
print()
print()
