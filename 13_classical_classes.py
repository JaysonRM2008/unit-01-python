
"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
print("------Task 1-------")
print()
print()
#created class
class Person:
    Race = 'hispanic'

    def __init__(self, name, age): #Define the function
         self.name = name 
         self.age = age
#person name, and age
Jayson = Person("Jayson", 17)
print(Jayson.name)
print(Jayson.age)
print(Jayson.Race)
        
print("------Task 1-------")
print()
print()
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
print("------Task 2-------")
print()
print()
#created the class
class Animal:
     def speak(self):
        return "Generic animal sound"

     
     #sub class #1
class Dog(Animal):
     def speak(self):  #Overrides the speak method to make a dog sound.
        
        return "Woof!"
class Cat(Animal):
     def speak(self): #Overrides the speak method to make a cat sound.
        return "Meow!"
# Create objects of the subclasses
my_dog = Dog()
my_cat = Cat()
# Call the speak method on each object
print(f"Dog says: {my_dog.speak()}")
print(f"Cat says: {my_cat.speak()}")

print("------Task 2-------")
print()
print()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
print("------Task 3-------")
print()
print()
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}.")


# Testing the class
account1 = BankAccount("Alice", 100)
account1.deposit(50)    # Should increase balance to 150
account1.withdraw(30)   # Should decrease balance to 120
account1.withdraw(200)  # Should show insufficient funds

account2 = BankAccount("Bob")
account2.deposit(200)   # Starting from 0, balance should be 200
account2.withdraw(100)  # Should reduce balance to 100

 


print("------Task 3-------")
print()
print()