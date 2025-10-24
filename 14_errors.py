"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
print("------Example 1-------")
print()
print()
def divide_numbers(num1, num2):
    #use try
    try:
        result = num1 / num2
        print("Result:", result)
        #use except
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Example usage:
divide_numbers(10, 2)
divide_numbers(10, 0)
print("------Example 1-------")
print()
print()
"""
Example 2: Opening Files
"""
print("------Example 2-------")
print()
print()
"""
Example 2: Opening Files
"""
def read_file(filename):
    try:
        file = open(filename, 'r') 
        contents = file.read()  
        print("File contents:", contents) # Prints the content
        #use FileNotFoundError
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. ")
# Example usage:
read_file("nonexistent.txt")

print("------Example 2-------")
print()
print()
"""
Example 3: List Items
"""
print("------Example 3-------")
print()
print()

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except IndexError:
        print("Error: Index {index} is out of range for the list. ")
# Example usage with an invalid index:
my_list = [1, 2, 3]
get_item(my_list, 5)
print("------Example 3-------")
print()
print()
"""
Example 4: Dictionaries
"""
print("------Example 4-------")
print()
print()

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
        #use keyerror
    except KeyError:
        print(f"Error: The key '{key}' dose not exist in the dictionary. ")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
print("------Example 4-------")
print()
print()

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
print("------Example 5-------")
print()
print()
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("File processed successfully (no exceptions encountered).")
    finally:
        print("File processing attempt finished.")


# Example usage:
process_file("example.txt") # This will likely result in FileNotFoundError unless "example.txt" exists
process_file("existing_file.txt") # Create this file for a successful execution example
print("------Example 5-------")
print()
print()
