from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = current_year - birth_year

# Display the result
print(f"You are {age} years old!")
