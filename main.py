# Getting user birth year
birth_year=int(input("Enter your birth year: "))
# Handling exceptions
if birth_year > 2026 or birth_year < 1920:
    print("Enter a valid year between 1920 and 2026")
else:
    age= 2026 - birth_year  # calculating age
    print(f"You are {age} years old!") # displaying age
