# Unique ID Generator System
# Generate unique ID
# Unique ID = 2 letters from first name + 2 letters from last name + 2 digits from birth year + 4 random digits

import random 

first_name = input('Enter your first name: ')
first_name_letters = first_name[0:2] 

last_name = input('Enter your last name: ')
last_name_letters = last_name[0:2]

birth_year = input('Enter your birth year (YYYY): ')
birth_year_digits = birth_year[2:4]

random_digits = random.randint(1000, 9999)

unique_id = first_name_letters + last_name_letters + birth_year_digits + str(random_digits)

print(f'Hello {first_name},\nYour new system-generated ID number is:\n{unique_id}')
# This code generates a unique ID based on the user's first name, last name, and birth year.