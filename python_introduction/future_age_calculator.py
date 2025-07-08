# Define the current year and the target year
current_year = 2023
target_year = 2050

# Calculate the difference in years
years_to_add = target_year - current_year

# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Calculate the user's age in 2050
future_age = current_age + years_to_add

# Print the result
print(f"In {target_year}, you will be {future_age} years old.")