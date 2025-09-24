def greet():
    print(f'''
{'*' * 70}
          Welcome to the Digital Recipe Management App!
          ==== ==== == Available commands: == ==== ====
          > "1" for add recipe
          > "2" for view recipes
          > "3" for search recipe
          > "4" for delete recipe
          > "5" for exit
{'*' * 70}
          ''')

def add_recipe():
  
    recipe = {} # Initialize recipe Dictionary
    recipe['name'] = input("Enter the recipe name: ").strip()
    recipe['type'] = input("Enter the recipe type (e.g., Dessert, Main Dish): ").strip()
    recipe['ingredeints'] = process_ingredients()
    recipe['steps'] = process_steps()

    recipe_storage.append(recipe) # add the new recipe to the global variable "recipe_storage"
    print(f'Recipe Added: {recipe['name']}!')
    
def process_ingredients():
    
    storage = []  # Create empty list for ingredients
    while True: # validation
        try:
            num_ingredients = int(input("How many ingredients? "))
            break
        except ValueError:  
            print("Invalid input! Please enter a number next time.")

    for i in range(num_ingredients):  # processing ingredients
        ingredient = input(f"Enter ingredient {i+1}: ").strip()
        storage.append(ingredient) 

    return storage

def process_steps():
    
    storage = []  # Create empty list for steps
    while True: # validation
        try:
            num_steps = int(input("How many steps? "))  
            break
        except ValueError:  
            print("Invalid input! Please enter a number next time.")
        
    for i in range(num_steps): # for processing steps
        step = input(f"Enter step {i+1}: ").strip()  
        storage.append(step)  
    
    return storage

def view_recipes():  # Function to display recipes
    if len(recipe_storage) == 0:  # Check if there are no recipes
        print("No recipes available.")
        return
    
    for i in range(len(recipe_storage)):  # Loop through each recipe
        recipe = recipe_storage[i]
        print(f"\nRecipe {i+1}: {recipe['name']}")
        print(f"Type: {recipe['type']}")

        # Display ingredients
        print("Ingredients:")
        ingredients = recipe['ingredients']
        if len(ingredients) == 0:
            print("  - No ingredients listed.")
        else:
            for item in ingredients:
                print(f"  - {item}")

        # Display steps
        print("Steps:")
        steps = recipe['steps']
        if len(steps) == 0:
            print("  1. No steps listed.")
        else:
            for idx in range(len(steps)):  # Loop through each step with numbering
                print(f"  {idx+1}. {steps[idx]}")

# main

recipe_storage = [ # container / storage for the recipes
                  {'name': 'Adobo', 'type': 'Main Dish', 'ingredients': ['Toyo', 'Suka', 'Asukal'], 'steps': ['Heat atsuete oil in pot', 'Add Garlic, Ginder and Onion']},
                  {'name': 'Sinigang', 'type': 'Soup', 'ingredients': ['Sinigang Mix', 'Baboy / Karne', 'Gulay'], 'steps': ['Simmer Pork', 'Add Vegetables']}
                ] 
while True:
    greet()
    command = int(input(F'Enter command > '))
    
    if command == 1:
        add_recipe()
        print(f'{recipe_storage[0]}')
    elif command == 2:
        view_recipes()
    elif command == 3:
        pass
    elif command == 4:
        pass
    elif command == 5:
        pass
    else:
        print(f'Invalid command!')
        
    
    
    
    
