def greet():
    print(f'''
\033[93m{'*' * 70}\033[0m
\033[1;92m    Welcome to the Digital Recipe Management App!\033[0m
\033[95m      ==== ==== == Available commands: == ==== ====\033[0m
\033[94m      > "1" for add recipe\033[0m
\033[94m      > "2" for view recipes\033[0m
\033[94m      > "3" for search recipe\033[0m
\033[94m      > "4" for delete recipe\033[0m
\033[91m      > "5" for exit\033[0m
\033[93m{'*' * 70}\033[0m
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
    print('\033[91m-\033[0m' * 20)     
    if not recipe_storage:  # Check if there are no recipes
        print("No recipes available.")
        return
    
    for i in range(len(recipe_storage)):  # Loop through each recipe
        recipe = recipe_storage[i]
        print(f"\033[93mRecipe {i+1}:\033[0m: {recipe['name']}")
        print(f"\033[93mType:\033[0m {recipe['type']}")

        # Display ingredients
        ingredients = recipe['ingredients']
        if not ingredients:
            print("No ingredients listed.")
        else:
           print(f'\033[93mIngredients:\033[0m {', '.join(ingredients)}')

        # Display steps
        steps = recipe['steps']
        if not steps:
            print("No steps listed.")
        else:
            steps_inline = " || ".join(f"{idx+1}. {step}" for idx, step in enumerate(steps))
            print(f"\033[93mSteps:\033[0m {steps_inline}")
        print('\033[91m-\033[0m' * 20)     
# main

recipe_storage = [ # container / storage for the recipes
                  {'name': 'Adobo', 'type': 'Main Dish', 'ingredients': ['Toyo', 'Suka', 'Asukal'], 'steps': ['Heat atsuete oil in pot', 'Add Garlic, Ginder and Onion']},
                  {'name': 'Sinigang', 'type': 'Soup', 'ingredients': ['Sinigang Mix', 'Baboy / Karne', 'Gulay'], 'steps': ['Simmer Pork', 'Add Vegetables']},
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
        break
    else:
        print(f'Invalid command!')
        
    
    
    
    
