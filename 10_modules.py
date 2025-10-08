import os
import sys

"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print("------Task 1-------")
print()
print()

# Get the current working directory
current_directory = os.getcwd()

# Print the current directory
print("Current working directory:", current_directory)

print("------Task 1-------")
print()
print()
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print("------Task 2-------")
print()
print()

# Create a new directory called 'test_folder' if it doesn't already exist
os.makedirs('test_folder', exist_ok=True)

# List all files and directories in the current directory
items = os.listdir('.')

# Print the list
print("Files and directories in current directory:")
for item in items:
    print(item)

print("------Task 2-------")
print()
print()
"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print("------Task 3-------")
print()
print()
# Define the directory name
dir_name = "data"

# Check if the directory exists
if os.path.isdir(dir_name):
    print("Directory already exists.")
else:
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created.")
print("------Task 3-------")
print()
print()
"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print("------Task 4-------")
print()
print()

# Define the filename
file_name = "config.txt"

# Check if the file exists
if os.path.isfile(file_name):
    # Get the absolute path
    file_path = os.path.abspath(file_name)
    print("File found at:", file_path)
else:
    print("File not found.")
print("------Task 4-------")
print()
print()
"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print("------Task 5-------")
print()
print()
print("Python Version:")
print(sys.version)

print("\nVersion Info (tuple format):")
print(sys.version_info)
print("------Task 5-------")
print()
print()

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print("------Task 6-------")
print()
print()
# Get the platform string
platform = sys.platform

# Map the platform string to user-friendly names
if platform.startswith('linux'):
    friendly_name = 'Linux'
elif platform == 'win32':
    friendly_name = 'Windows'
elif platform == 'darwin':
    friendly_name = 'MacOS'
else:
    friendly_name = f'Unknown platform: {platform}'

# Print the result
print(f"You are running on: {friendly_name}")

print("------Task 6-------")
print()
print()