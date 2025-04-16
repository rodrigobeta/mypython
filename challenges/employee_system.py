# Employee Management System

# Create employee variables
employee_name = input('Enter employee name: ')
employee_age = int(input('Enter employee age: '))
employee_salary = float(input('Enter employee salary: '))

"""
    input() collects user response

    .strip() removes leading and trailing whitespace

    .lower() converts text to lowercase to make comparison case-insensitive

    The comparison == 'yes' will return True if user typed "yes" 
    (in any upper/lowercase format) or False otherwise

"""
department_head = input("Are you a department head? (Yes/No): ").strip().lower()
is_department_head = department_head == 'yes'

# Print employee information
print(f'Employee name: {employee_name}')
print(f'Employee age: {employee_age}')
print(f'Employee salary: {employee_salary:.2f}')
print(f'Is department head?: {is_department_head}')