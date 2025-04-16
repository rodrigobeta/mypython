# Cooking Recipe Manager
# This program collects and displays recipe information

# Get recipe details from user
recipe_name = input('Enter recipe name: ').strip()
ingredients = input('Enter ingredients (separate with spaces): ').strip()
cooking_time = float(input('Enter cooking time (in minutes): '))
difficulty = input('Enter difficulty (Easy/Medium/Hard): ').strip()

# Print recipe information
print('\nRecipe Details:')
print('-' * 20)
print(f'Recipe name: {recipe_name}')
print(f'Ingredients: {ingredients.replace(" ", ", ")}')
print(f'Cooking time: {cooking_time:.2f} minutes')
print(f'Difficulty: {difficulty}')


