import sys
from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Check if a birth year argument is provided
if len(sys.argv) < 2:
    print("Error: Please provide a birth year as an argument.")
    sys.exit(1)

try:
    birth_year = int(sys.argv[1])  # Read birth year from command-line argument
    if birth_year > current_year:
        print("Error: Birth year cannot be in the future!")
    else:
        age = current_year - birth_year
        print(f"You are {age} years old!")
except ValueError:
    print("Error: Please enter a valid number!")
    sys.exit(1)
