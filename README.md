### ProgCon-Recipe-System
#### prerequisites
- fork this repository
- create an empty folder
- clone this repostiory using this command: git clone git@github.com:Aicyraa/ProgCon-Recipe-System.git

 ## commands for git  
```bash
 
 - git add 
    
    >> para ma-add sa staging area (2nd stage)

 - git commit -m 'msg' 

    >> para ma totally save sa local repository ninyo (git)

 - git status
    
    >> para makita nyo kung ano ung mga files na wala pa sa staging area (2nd stage),  e.g mga kagagawa lang na file or mga nabagong file

 - git push origin main

    >> para mapunta sa remote repository (github) ung code na nabago / ginawa ninyo

 - git pull origin main

    >> para ma kuha nyo ung updated code mula sa remote repository (github) papunta local repository (git)

 - pull request (contribute) sa github na to, kung finalize na ung code dun kayo mag pull request.

    >> para ma combine / merge ung code na ginawa  nyo sa main repostiory 
``` 

<br>
<br>
<br>

## Step by step guide  

> Run the Python program in your terminal/console.  
> See the main menu  
> You’ll see numbered choices: Add Recipe, View Recipes,   Search Recipe, Delete Recipe, Exit.

```python

>> function 1: def greet():

   1. for printing the commands:
      > add recipe
      > view recipe
      > search recipe
      > delete recite

>> funcition 2: Add a recipe (choose Add Recipe)

   1. Enter the recipe name when asked.
   2. Enter the recipe type (e.g., Dessert, Main Dish).
   3. When asked “How many ingredients?” type an integer (e.g., 3) and press Enter.
   4. Enter each ingredient one by one when prompted.
   5. When asked “How many steps?” type an integer (e.g., 4) and press Enter.
   6. Enter each cooking step one by one.
   7. Program confirms: Recipe 'X' added!

>> function 3: View all recipes (choose View Recipes)

   1. The app lists every recipe with its type, a bulleted ingredient list, and numbered steps.


>> function 4: Search for a recipe (choose Search Recipe)

   1. Type the recipe name to search.
   2. The search compares names case-insensitively, so adobo and Adobo match.
   3. If found, the recipe details are shown; if not, you’ll see “Recipe not found.”

>> function 5: Delete a recipe (choose Delete Recipe)

   1. Type the exact recipe name to delete (case insensitive).
   2. If it exists the app removes it and confirms deletion; otherwise it shows “Recipe not found.”

>> Exit the program (choose Exit)
>> The program stops and returns you to the terminal.

```

> Important usage notes 

- When asked for numbers (ingredients/steps), enter a valid integer — invalid input may cause an error unless the program has validation.
- To cancel an input operation immediately, use Ctrl+C in the terminal.
- Names are matched case-insensitively but must otherwise match (beware typos).
- Recipes are stored in memory (a list of dictionaries). They will be lost when the program exits unless you add save/load functionality.

Quick demo sequence for presentation
Show: Add one recipe → Add a second → View Recipes → Search for the first → Delete the second → View Recipes → Exit.
