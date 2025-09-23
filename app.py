def greet():
    print(f'''
          Welcome to the Digital Recipe Management App!
          ==== ==== == Available commands: == ==== ====
          > "1" for add recipe
          > "2" for view recipes
          > "3" for search recipe
          > "4" for delete recipe
          > "5" for exit
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
        pass
    elif command == 3:
        pass
    elif command == 4:
        pass
    elif command == 5:
        pass
    else:
        print(f'Invalid command!')
        
    
    
    
    
