# Email Generator
# This script generates a company email address from a user's full name

user_name = 'Ubaldo Acosta Soto'
company_name = 'Global Mentoring'
domain = '.com.mx'

# Format username (lowercase and replace spaces with dots)
user_name = user_name.lower()
user_name = user_name.replace(' ', '.')

# Format company name (lowercase and remove spaces)
company_name = company_name.lower()
company_name = company_name.replace(' ', '')

# Generate and print the email
print(f'Email address: {user_name}@{company_name}{domain}')