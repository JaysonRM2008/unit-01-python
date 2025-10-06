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