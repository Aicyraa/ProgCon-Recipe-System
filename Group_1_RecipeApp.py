def greet(): # for system information
    print(f'''
    \033[93m{'*' * 70}\033[0m
    \033[1;92mWelcome to the Digital Recipe Management App!\033[0m
    \033[95m==== ==== == Available commands: == ==== ====\033[0m
    \033[94m> "1" for add recipe\033[0m
    \033[94m> "2" for view recipes\033[0m
    \033[94m> "3" for search recipe\033[0m
    \033[94m> "4" for delete recipe\033[0m
    \033[91m> "5" for exit\033[0m
    \033[93m{'*' * 70}\033[0m
          ''')

def add_recipe(): # for adding recipe
    recipe = {}
    recipe['name'] = input("Enter the recipe name: ").strip()
    recipe['type'] = input("Enter the recipe type (e.g., Dessert, Main Dish): ").strip()
    recipe['ingredients'] = process_ingredients()  # fixed typo
    recipe['steps'] = process_steps()

    recipe_storage.append(recipe) # append the recipe dictionary to the recipe_storage list
    print(f"\033[92mRecipe Added: {recipe['name']}!\033[0m")
    
def process_ingredients(): # for processing ingredients
    storage = []
    while True: 
        try: # validation
            num_ingredients = int(input("How many ingredients? "))
            break
        except ValueError:  
            print("\033[91mInvalid input! Please enter a number next time.\033[0m")

    for i in range(num_ingredients): # for inserting ingredients
        ingredient = input(f"Enter ingredient {i+1}: ").strip()
        storage.append(ingredient) 

    return storage

def process_steps(): # for processing steps
    storage = []
    while True:
        try: # validation
            num_steps = int(input("How many steps? "))  
            break
        except ValueError:  
            print("\033[91mInvalid input! Please enter a number next time.\033[0m")
        
    for i in range(num_steps): # for inserting steps
        step = input(f"Enter step {i+1}: ").strip()  
        storage.append(step)  
    
    return storage

def view_recipes(): # for viewing all the recipes
    print('\033[91m-\033[0m' * 20)     
    if not recipe_storage: # if there is no recipe
        print("\033[91mNo recipes available.\033[0m")
        return
    
    for i, recipe in enumerate(recipe_storage, start=1): # for displaying ingredients and steps per recipe
        print(f"\033[93mRecipe {i}:\033[0m {recipe['name']}")
        print(f"\033[93mType:\033[0m {recipe['type']}")

        ingredients = recipe['ingredients'] # for displaying ingredients
        if not ingredients:
            print("\033[91mNo  ingredients listed.\033[0m")
        else:
            print(f"\033[93mIngredients:\033[0m {', '.join(ingredients)}")

        steps = recipe['steps']
        if not steps: # for displaying steps
            print("\033[91mNo steps listed.\033[0m")
        else:
            steps_inline = " || ".join(f"{idx+1}. {step}" for idx, step in enumerate(steps))
            print(f"\033[93mSteps:\033[0m {steps_inline}")
        print('\033[91m-\033[0m' * 20)     

def search_recipe():
    recipe_name = input("Enter recipe you want to search: ").strip().lower()
    for recipe in recipe_storage:
        if recipe['name'].lower() == recipe_name: # if recipe_name match recipe['name'], display recipe info then return
            print("\033[92m=== Recipe Found! ===\033[0m")
            print(f"\033[93mName:\033[0m {recipe['name']}")
            print(f"\033[93mType:\033[0m {recipe['type']}")
            print(f"\033[93mIngredients:\033[0m {', '.join(recipe['ingredients'])}")
            print(f"\033[93mSteps:\033[0m {', '.join(recipe['steps'])}")
            return 
        
    print("\033[91mRecipe not found.\033[0m")


def delete_recipe():
    name_to_delete = input("Enter the recipe name to delete: ").strip().lower()
    
    if not recipe_storage: # if recipe_storage is empty
        print("\033[91mNo recipes available to delete.\033[0m")
        return
    
    for recipe in recipe_storage:
        if recipe['name'].lower() == name_to_delete: # if name_to_delete match recipe['name'], remove, display and return
            recipe_storage.remove(recipe)
            print(f"\033[93mRecipe '{recipe['name']}' deleted successfully!\033[0m")
            return
    
    print("\033[91mRecipe not found.\033[0m")


# main
recipe_storage = [ # storage for rrecipes
    {'name': 'Adobo', 'type': 'Main Dish', 'ingredients': ['Toyo', 'Suka', 'Asukal'], 'steps': ['Heat atsuete oil in pot', 'Add Garlic, Ginger and Onion']}, # dummy recipe value
    {'name': 'Sinigang', 'type': 'Soup', 'ingredients': ['Sinigang Mix', 'Baboy / Karne', 'Gulay'], 'steps': ['Simmer Pork', 'Add Vegetables']}, # dummy value
] 

greet()
while True:
    try: # validation
        command = int(input("Enter command > "))
    except ValueError:
        print("\033[91mInvalid input! Please enter a number.\033[0m")
        continue
    
    if command == 1:
        add_recipe()
    elif command == 2:
        view_recipes()
    elif command == 3:
        search_recipe()
    elif command == 4:
        delete_recipe()
    elif command == 5:
        print("\033[91mExiting program... Goodbye!\033[0m")
        break # exiting the loop
    else:
        print("\033[91mInvalid command!\033[0m")
