# String methods examples

text = "Hello World"
name = "john doe"
spaces = "    python    "
numbers = "123"
mixed = "Python123"

# Common string methods
print("Upper:", text.upper())         # HELLO WORLD
print("Lower:", text.lower())         # hello world
print("Title:", name.title())         # John Doe
print("Capitalize:", name.capitalize())    # John doe

# Remove whitespace
print("Strip:", spaces.strip())           # "python"
print("Left strip:", spaces.lstrip())     # "python    "
print("Right strip:", spaces.rstrip())    # "    python"

# Search and replace
print("Replace:", text.replace("World", "Python"))    # Hello Python
print("Count 'l':", text.count('l'))                 # 3
print("Find 'World':", text.find("World"))          # 6
print("Contains 'Hello':", "Hello" in text)         # True

# Check content type
print("Is alpha:", text.isalpha())        # False (contains space)
print("Is numeric:", numbers.isnumeric()) # True
print("Is alphanumeric:", mixed.isalnum()) # True

# Split and join
words = text.split()                      # ['Hello', 'World']
print("Split:", words)
print("Join:", "-".join(words))           # Hello-World

# Format
name = "Alice"
age = 25
print("Format: {}".format(name))                      # Alice
print(f"F-string: {name} is {age} years old")        # Alice is 25 years old

"""
    Case Methods

.upper(): Converts to uppercase
.lower(): Converts to lowercase
.title(): Capitalizes first letter of each word
.capitalize(): Capitalizes first letter of string
Whitespace Methods

.strip(): Removes leading and trailing whitespace
.lstrip(): Removes leading whitespace
.rstrip(): Removes trailing whitespace
Search Methods

.find(): Returns index of substring
.count(): Counts occurrences of substring
.replace(): Replaces substring with new text
Validation Methods

.isalpha(): Checks if string contains only letters
.isnumeric(): Checks if string contains only numbers
.isalnum(): Checks if string contains letters or numbers
Split and Join

.split(): Splits string into list
.join(): Joins list elements into string
Formatting

.format(): Old style formatting
f"...": F-strings (modern string formatting)

"""