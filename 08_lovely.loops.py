# Get the survey name from the user
survey_name = input("Enter survey name: ")

# Get the number of responses expected
num_responses = int(input("Enter number of responses: "))

# Initialize variables to store total ratings and count of new customers
total_rating = 0
new_customers = 0

# Loop over the number of responses
for x in range(num_responses):
    # Ask if customer is returning or new
    customer_type = input("Is it a returning or new customer?: ")
    
    # Get the rating for this response
    rating = int(input("What is the rating?(1-5): "))
    
    # Add the rating to the total_rating
    total_rating += rating
    
    # Check if rating is invalid
    if total_rating < 1 and total_rating > 5:
        print("Invalid")
    
    # If customer is new, increment new_customers count
    if customer_type == "new":
        new_customers +=1
    else:
        # Do nothing if customer is returning
        new_customers +=0

# Calculate the average rating
avg_rating = total_rating / num_responses

# Print the average rating
print(avg_rating)
