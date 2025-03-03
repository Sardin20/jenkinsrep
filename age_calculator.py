import sys
from datetime import datetime

# Get the current year and current date-time
current_date = datetime.now()
current_year = current_date.year

# Check if a birth year argument is provided
if len(sys.argv) < 2:
    print("Error: Please provide a birth year as an argument.")
    sys.exit(1)

try:
    birth_year = int(sys.argv[1])  # Read birth year from command-line argument
    birth_date = datetime(birth_year, 1, 1)  # Assume January 1st of birth year

    if birth_year > current_year:
        print("Error: Birth year cannot be in the future!")
    else:
        # Calculate age in years
        age = current_year - birth_year

        # Calculate total time spent on Earth
        time_spent = current_date - birth_date
        days_lived = time_spent.days
        hours_lived = days_lived * 24
        minutes_lived = hours_lived * 60
        seconds_lived = minutes_lived * 60

        # Display results
        print(f"You are {age} years old.")
        print(f"Total time spent on Earth:")
        print(f"- {days_lived} days")
        print(f"- {hours_lived} hours")
        print(f"- {minutes_lived} minutes")
        print(f"- {seconds_lived} seconds")

except ValueError:
    print("Error: Please enter a valid number!")
    sys.exit(1)
