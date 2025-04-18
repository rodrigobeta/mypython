import random
import string
import datetime

def validate_name(name):
    """Validate that name contains only letters."""
    return name.isalpha()

def validate_year(year):
    """Validate birth year is realistic."""
    current_year = datetime.datetime.now().year
    try:
        year = int(year)
        return 1900 <= year <= current_year
    except ValueError:
        return False

def generate_unique_id(first_name, last_name, birth_year):
    """Generate unique ID with additional security features."""
    # Get first 2 letters of names (converted to uppercase)
    first_letters = first_name[:2].upper()
    last_letters = last_name[:2].upper()
    
    # Get last 2 digits of birth year
    year_digits = str(birth_year)[-2:]
    
    # Generate 4 random digits
    random_digits = str(random.randint(1000, 9999))
    
    # Add a random letter for extra uniqueness
    random_letter = random.choice(string.ascii_uppercase)
    
    # Combine all parts
    return f"{first_letters}{last_letters}-{year_digits}{random_letter}{random_digits}"

def main():
    print("Welcome to the Advanced ID Generator System")
    print("-" * 40)

    # Get and validate first name
    while True:
        first_name = input('Enter your first name: ').strip()
        if validate_name(first_name):
            break
        print("Error: Please enter a valid name (letters only)")

    # Get and validate last name
    while True:
        last_name = input('Enter your last name: ').strip()
        if validate_name(last_name):
            break
        print("Error: Please enter a valid name (letters only)")

    # Get and validate birth year
    while True:
        birth_year = input('Enter your birth year (YYYY): ').strip()
        if validate_year(birth_year):
            birth_year = int(birth_year)
            break
        print("Error: Please enter a valid year between 1900 and current year")

    # Generate and display ID
    unique_id = generate_unique_id(first_name, last_name, birth_year)
    
    print("\nID Generation Successful!")
    print("-" * 40)
    print(f"Name: {first_name.title()} {last_name.title()}")
    print(f"Birth Year: {birth_year}")
    print(f"Your Unique ID: {unique_id}")
    print("\nPlease keep this ID secure and confidential.")

if __name__ == "__main__":
    main()